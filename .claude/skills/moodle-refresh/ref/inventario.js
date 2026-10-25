// Inventário das UCs do Moodle → só o que é NOVO ou MUDOU desde o último refresh.
// Corre numa página qualquer do moodle2627 (sessão do Gonçalo), com o javascript_tool.
// Antes de correr, substituir as duas constantes pela saída de `moodle.py conhecidos`.
// Correr DEPOIS do extrair.js (usa o lote dele). Resultado: escrito no <body> (ler com
// get_page_text: o javascript_tool corta a ~1000 caracteres) e um `moodle__estado__<D>.json`
// por UC posto no lote (o `moodle.py arrumar` guarda-o; o `fechar` só o aplica no fim).
const CURSOS = [];      // [[6243, "Redes"], ...]
const CONHECIDOS = {};  // {"Redes": {"65421": "assinatura", ...}, ...}

const P = s => new DOMParser().parseFromString(s, "text/html");
const txt = el => (el ? el.innerText || el.textContent : "").replace(/\s+/g, " ").trim();
const hash = s => { let h = 5381; for (const c of s) h = (h * 33 ^ c.codePointAt(0)) >>> 0; return h.toString(36); };
const get = async u => P(await (await fetch(u)).text());
async function revisao(cm) {  // "<revisão>/<ficheiro>" do pluginfile, sem descarregar o corpo
  const c = new AbortController();
  try {
    const r = await fetch(`/mod/resource/view.php?id=${cm}&redirect=1`, { signal: c.signal });
    const p = new URL(r.url).pathname; c.abort();
    return p.includes("pluginfile") ? decodeURIComponent(p.replace(/^.*\/content\//, "")) : "sem-ficheiro";
  } catch (e) { return "ERRO"; }
}
const ficheiros = el => [...el.querySelectorAll("a[href*='pluginfile']")]
  .map(a => decodeURIComponent(a.pathname.replace(/^.*pluginfile\.php/, "")));

let out = `Refresh Moodle ${new Date().toLocaleString("pt-PT")}\n`;
for (const [id, D] of CURSOS) {
  const conh = CONHECIDOS[D] || {}, novo = {}, ocultos = [];
  let linhas = "";
  const d = await get(`/course/view.php?id=${id}`);
  for (const s of d.querySelectorAll("li.section")) {
    const sec = txt(s.querySelector(".sectionname, h3")) || "?";
    const sum = s.querySelector(".summarytext, .summary");
    if (sum && txt(sum)) {
      const k = "sec:" + (s.id || sec), sig = hash(txt(sum));
      novo[k] = sig;
      if (conh[k] !== sig) linhas += `${conh[k] ? "MUDOU" : "NOVO"} | secção | ${sec} | ${txt(sum).slice(0, 700)}${ficheiros(sum).length ? " [ficheiros: " + ficheiros(sum).join(", ") + "]" : ""}\n`;
    }
    for (const a of s.querySelectorAll("li.activity")) {
      const tipo = (a.className.match(/modtype_(\w+)/) || [])[1];
      const cm = (a.id.match(/\d+/) || [""])[0];
      const link = a.querySelector("a.aalink");
      const nome = txt(a.querySelector(".instancename")).replace(/ (Ficheiro|Página|Pasta|URL|Trabalho|Fórum|Teste|Escolha de grupos|Ficha da unidade)$/, "");
      const datas = txt(a.querySelector("[data-region='activity-dates']"));
      if (!link && tipo !== "label") { ocultos.push(nome); continue; }
      let sig, det = "";
      if (tipo === "label") {
        const box = a.querySelector(".activity-altcontent, .contentwithoutlink, .no-overflow") || a;
        det = txt(box).replace(/^Selecionar a atividade .*? (?=\S)/, "").slice(0, 900);
        const fs = ficheiros(box); if (fs.length) det += " [ficheiros: " + fs.join(", ") + "]";
        sig = hash(det);
      } else if (tipo === "resource") { sig = await revisao(cm); det = sig; }
      else if (tipo === "folder") { const f = await get(link.href); det = ficheiros(f.querySelector("#region-main")).join(", "); sig = hash(det); }
      else if (tipo === "page") { const f = await get(link.href); sig = hash(txt(f.querySelector("#region-main .generalbox, #region-main .box"))); }
      else if (tipo === "assign") {
        const f = await get(link.href); const intro = f.querySelector(".activity-description, #intro");
        det = txt(f.querySelector("[data-region='activity-dates'], .activity-dates")) || datas;
        sig = hash(txt(intro) + det); if (intro && ficheiros(intro).length) det += " [ficheiros: " + ficheiros(intro).join(", ") + "]";
      } else if (tipo === "forum") {
        const f = await get(link.href);
        const ds = [...f.querySelectorAll("[data-region='discussion-list-item']")]
          .map(t => [t.getAttribute("data-discussionid"), txt(t).replace(/ Bloqueado.*$/, "").slice(0, 90)]);
        const antes = (conh[cm] || "").split(",");
        sig = ds.map(x => x[0]).join(",");
        det = ds.filter(x => !antes.includes(x[0])).map(x => `#${x[0]} ${x[1]}`).join(" ; ");
      } else if (tipo === "url") { det = txt(a.querySelector(".activity-description")); sig = hash(nome + det); }
      else sig = hash(nome + datas);
      novo[cm] = sig;
      if (conh[cm] !== sig) linhas += `${conh[cm] ? "MUDOU" : "NOVO"} | ${cm} | ${tipo} | ${sec} | ${nome}${det ? " | " + det : ""}${datas ? " | " + datas : ""}\n`;
    }
  }
  out += `\n===== ${D} (curso ${id})\n${linhas || "(nada de novo)\n"}`;
  if (ocultos.length) out += `ainda sem acesso: ${ocultos.join("; ")}\n`;
  guarda(`moodle__estado__${D}.json`, new Blob([JSON.stringify(novo, null, 1)], { type: "application/json" }));
}
document.body.innerHTML = "<article><pre id=x></pre></article>";
document.getElementById("x").textContent = out;
out.length;
