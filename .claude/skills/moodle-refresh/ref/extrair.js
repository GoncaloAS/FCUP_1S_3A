// Funções para trazer material do Moodle. Injetar UMA vez por sessão (ficam em window enquanto
// a página não muda: não navegar depois; tudo é por fetch). Nada é descarregado logo: cada
// ficheiro entra no LOTE com o nome  moodle__<D>__<destino com / trocado por ~>  e no fim
// `entregar()` descarrega UM só moodle__lote_<hora>.zip para ~/Downloads (o Chrome bloqueia
// descargas automáticas a seguir à primeira). O `moodle.py arrumar` abre o lote e põe cada
// ficheiro no sítio. Destino relativo à pasta da disciplina, p. ex. "Teoricas/Aula_04.pdf".
//   await recurso("Redes", 65421, "Teoricas/Aula_04.pdf")        ficheiro (mod/resource)
//   await ficheiro("Redes", "/134416/mod_label/intro/x.pdf", "Testes/Teste_Modelo_1.pdf")
//   await pagina("Redes", 65437, "Praticas/Semana_7/ficha_7_<tema>.pdf")   página → .md → PDF
//   await pagina("Redes", 65410, "Trabalho/enunciado.pdf", "assign")      enunciado de trabalho
//   ler("/mod/forum/discuss.php?d=1923")   mostra a página em markdown no <body> (get_page_text)
//   avisos([2628, 2013])   mostra no <body> o texto das discussões de fórum (ids do inventário)
//   lote()        o que está no lote;   entregar()   descarrega o lote (uma vez, no fim)
window.P = s => new DOMParser().parseFromString(s, "text/html");
window.md = function (n, ctx) {
  ctx = ctx || { ol: 0 };
  if (n.nodeType == 3) return n.textContent.replace(/\s+/g, " ");
  if (n.nodeType != 1) return "";
  const t = n.tagName.toLowerCase(), kids = () => [...n.childNodes].map(c => md(c, ctx)).join("");
  switch (t) {
    case "h1": case "h2": case "h3": case "h4": case "h5":
      return "\n\n" + "#".repeat(Math.max(2, +t[1])) + " " + kids().trim() + "\n\n";
    case "p": case "div": case "section": case "article": return "\n\n" + kids().trim() + "\n\n";
    case "br": return "\n";
    case "strong": case "b": { const k = kids().trim(); return k ? "**" + k + "** " : ""; }
    case "em": case "i": { const k = kids().trim(); return k ? "*" + k + "* " : ""; }
    case "sup": return "^" + kids() + "^";
    case "code": case "tt": case "kbd": return "`" + n.textContent + "`";
    case "pre": return "\n\n```\n" + n.textContent.replace(/\n$/, "") + "\n```\n\n";
    case "a": {
      let h = ""; try { const u = new URL(n.getAttribute("href") || "", location.href); h = u.origin === location.origin ? u.pathname : u.href; } catch (e) {}
      return "[" + kids().trim() + "](" + h + ")";
    }
    case "img": { let p = ""; try { p = new URL(n.src).pathname; } catch (e) {} return "\n\n![" + (n.alt || "") + "](" + p + ")\n\n"; }
    case "ol": case "ul": {
      const d = ctx.ol, typ = n.getAttribute("type") || getComputedStyle(n).listStyleType; let i = +(n.getAttribute("start") || 1) - 1;
      const it = [...n.children].filter(c => c.tagName == "LI").map(li => {
        i++;
        const m = t == "ul" ? "-" : /^a|alpha/.test(typ) ? String.fromCharCode(96 + i) + ")" : /^i|roman/.test(typ) ? ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"][i - 1] + ")" : i + ".";
        ctx.ol++; const s = [...li.childNodes].map(c => md(c, ctx)).join("").trim().replace(/\n{2,}/g, "\n").replace(/\n/g, "\n" + "   ".repeat(d + 1)); ctx.ol--;
        return "   ".repeat(d) + m + " " + s;
      });
      return "\n\n" + it.join("\n") + "\n\n";
    }
    case "dl": return "\n\n" + [...n.children].map(c => c.tagName == "DT" ? "- **" + c.innerText.trim() + "** — " : md(c, ctx).trim() + "\n").join("") + "\n\n";
    case "table": return "\n\n" + [...n.querySelectorAll("tr")].map(r => "| " + [...r.children].map(c => md(c, ctx).replace(/\s*\n\s*/g, " ").trim().replace(/\|/g, "\\|")).join(" | ") + " |").join("\n") + "\n\n";
    case "script": case "style": case "button": return "";
    default: return kids();
  }
};
window._lote = window._lote || new Map();
window.guarda = (nome, blob) => { _lote.set(nome, blob); };
window.lote = () => [..._lote].map(([n, b]) => `${n} (${Math.round(b.size / 1024)}KB)`).join("\n") || "(vazio)";
window.entregar = async function () {  // ZIP sem compressão ("store"), nomes em UTF-8
  const T = new Uint32Array(256).map((_, n) => { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; return c; });
  const crc = b => { let c = ~0; for (const x of b) c = T[(c ^ x) & 255] ^ (c >>> 8); return ~c >>> 0; };
  const enc = new TextEncoder(), partes = [], central = []; let off = 0;
  for (const [nome, blob] of _lote) {
    const n = enc.encode(nome), d = new Uint8Array(await blob.arrayBuffer()), c = crc(d);
    const h = new DataView(new ArrayBuffer(30));
    [[0, 0x04034b50, 4], [4, 20, 2], [6, 0x800, 2], [14, c, 4], [18, d.length, 4], [22, d.length, 4], [26, n.length, 2]]
      .forEach(([o, v, t]) => t == 4 ? h.setUint32(o, v, true) : h.setUint16(o, v, true));
    const ch = new DataView(new ArrayBuffer(46));
    [[0, 0x02014b50, 4], [4, 20, 2], [6, 20, 2], [8, 0x800, 2], [16, c, 4], [20, d.length, 4], [24, d.length, 4], [28, n.length, 2], [42, off, 4]]
      .forEach(([o, v, t]) => t == 4 ? ch.setUint32(o, v, true) : ch.setUint16(o, v, true));
    partes.push(h, n, d); central.push(ch, n); off += 30 + n.length + d.length;
  }
  const tam = central.reduce((s, x) => s + x.byteLength, 0), e = new DataView(new ArrayBuffer(22));
  [[0, 0x06054b50, 4], [8, _lote.size, 2], [10, _lote.size, 2], [12, tam, 4], [16, off, 4]]
    .forEach(([o, v, t]) => t == 4 ? e.setUint32(o, v, true) : e.setUint16(o, v, true));
  const zip = new Blob([...partes, ...central, e], { type: "application/zip" });
  const nome = `moodle__lote_${new Date().toISOString().slice(0, 16).replace(/\D/g, "")}.zip`;
  const u = URL.createObjectURL(zip), a = document.createElement("a");
  a.href = u; a.download = nome; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(u), 120000);
  const r = `${nome}: ${_lote.size} ficheiros, ${Math.round(zip.size / 1024)}KB`; _lote.clear(); return r;
};
window.alvo = (D, destino) => `moodle__${D}__${destino.replace(/\//g, "~")}`;
window.recurso = async function (D, cm, destino) {
  const r = await fetch(`/mod/resource/view.php?id=${cm}&redirect=1`), b = await r.blob();
  guarda(alvo(D, destino), b);
  return `${destino} ← ${decodeURIComponent(new URL(r.url).pathname.split("/").pop())} (${Math.round(b.size / 1024)}KB)`;
};
window.ficheiro = async function (D, caminho, destino) {
  const r = await fetch("/pluginfile.php" + caminho.replace(/^.*pluginfile\.php/, "")), b = await r.blob();
  guarda(alvo(D, destino), b);
  return `${destino} (${Math.round(b.size / 1024)}KB)`;
};
window.pagina = async function (D, cm, destinoPdf, tipo = "page") {
  const d = P(await (await fetch(`/mod/${tipo}/view.php?id=${cm}`)).text());
  const titulo = (d.querySelector("#region-main h2, .page-header-headings h1, h1")?.innerText || "").trim();
  const box = tipo === "assign" ? d.querySelector(".activity-description, #intro") : d.querySelector("#region-main .generalbox, #region-main .box");
  const datas = [...d.querySelectorAll("[data-region='activity-dates'] div, .activity-dates div")].map(x => x.innerText.trim()).filter(Boolean);
  const alt = (d.querySelector(".modified")?.innerText || "").trim();
  let s = md(box).replace(/\n{3,}/g, "\n\n").trim();
  const imgs = [...s.matchAll(/!\[[^\]]*\]\((\/pluginfile\.php[^)]+)\)/g)].map(m => m[1]);
  for (const p of new Set(imgs)) {
    const nome = `${cm}-${decodeURIComponent(p.split("/").pop())}`;
    guarda(alvo(D, ".fonte/moodle/img/" + nome), await (await fetch(p)).blob());
    s = s.split(p).join("img/" + nome);
  }
  const anexos = [...new Set([...s.matchAll(/\]\((\/pluginfile\.php[^)]+)\)/g)].map(m => m[1]))];
  const cab = `# ${titulo}\n\n*${[alt, ...datas].filter(Boolean).join(" · ") || "Moodle"}*\n\n`;
  guarda(alvo(D, destinoPdf.replace(/\.pdf$/, ".md")), new Blob([cab + s + "\n"], { type: "text/markdown" }));
  return `${destinoPdf}: ${s.length} car., ${imgs.length} imagens` + (anexos.length ? `; anexos por trazer com ficheiro(): ${anexos.join(" ")}` : "");
};
window.ler = async function (url, sel = "#region-main") {
  const d = P(await (await fetch(url)).text());
  const s = md(d.querySelector(sel)).replace(/\n{3,}/g, "\n\n");
  document.body.innerHTML = "<article><pre id=x></pre></article>";
  document.getElementById("x").textContent = s;
  return s.length;
};
window.avisos = async function (ids) {
  let out = "";
  for (const id of ids) {
    const p = P(await (await fetch(`/mod/forum/discuss.php?d=${id}`)).text());
    for (const x of p.querySelectorAll(".forumpost")) {
      const h = (x.querySelector("[data-region-content='forum-post-core-subject'], h3, .subject")?.innerText || "").trim();
      const quando = (x.querySelector("time")?.getAttribute("datetime") || "").slice(0, 10);
      const quem = (x.querySelector(".author a, header a[href*='user/view']")?.innerText || "").trim();
      out += `\n### #${id} ${h} — ${quem} ${quando}\n` + md(x.querySelector(".post-content-container") || x).replace(/\n{3,}/g, "\n\n").trim().slice(0, 3000) + "\n";
    }
  }
  document.body.innerHTML = "<article><pre id=x></pre></article>";
  document.getElementById("x").textContent = out;
  return out.length;
};
"extrair.js pronto";
