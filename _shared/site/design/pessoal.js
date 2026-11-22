// Painel pessoal: decifra assets/pessoal.enc (AES-GCM, chave PBKDF2 da palavra-passe; ver
// _shared/template/pessoal.py) e preenche o que a página tiver: o painel do início (#painel),
// a agenda completa (#agenda-pagina) e o separador Info das disciplinas ([data-info]).
// A chave derivada fica no localStorage deste browser; "Bloquear" apaga-a.
import { notas } from "./notas.js";
const ENC = new URL("pessoal.enc", import.meta.url);
const CHAVE = "painel-chave", FEITAS = "painel-feitas", MINHAS = "painel-minhas";

const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));
const ler = (k, def) => { try { return JSON.parse(localStorage.getItem(k)) ?? def; } catch (e) { return def; } };
const guardar = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; };

async function deriva(pw, enc) {
  const base = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits({ name: "PBKDF2", salt: b64(enc.sal), iterations: enc.it, hash: "SHA-256" }, base, 256);
  return new Uint8Array(bits);
}
async function decifra(raw, enc) {
  const k = await crypto.subtle.importKey("raw", raw, "AES-GCM", false, ["decrypt"]);
  const pt = await crypto.subtle.decrypt({ name: "AES-GCM", iv: b64(enc.iv) }, k, b64(enc.ct));
  return JSON.parse(new TextDecoder().decode(pt));
}

// ---- datas
const HOJE = new Date(); HOJE.setHours(0, 0, 0, 0);
const DIAS = ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"];
const dia = iso => new Date(iso + "T00:00:00");
const dif = iso => Math.round((dia(iso) - HOJE) / 864e5);
const curta = iso => { const d = dia(iso); return `${DIAS[d.getDay()]} ${d.getDate()}/${d.getMonth() + 1}`; };
function falta(iso) {
  const n = dif(iso);
  return n === 0 ? "hoje" : n === 1 ? "amanhã" : n > 1 ? `faltam ${n} dias` : n === -1 ? "ontem" : `há ${-n} dias`;
}

let D = null;                       // dados decifrados
const cores = (() => { try { return JSON.parse(document.querySelector("[data-cores]")?.dataset.cores || "{}"); } catch (e) { return {}; } })();
const nome = d => (D && D.nomes[d]) || d;
const comCor = (e, d) => { if (cores[d] != null) e.dataset.cor = cores[d]; return e; };
const raiz = new URL("..", import.meta.url).href;   // assets/ -> raiz do site
const abs = h => !h ? "" : /^(https?:|\.\.?\/)/.test(h) ? h : raiz + h;

// ---- painel do início
function agendaProxima(ol) {
  ol.replaceChildren();
  const prox = D.agenda.filter(e => dif(e.data) >= 0 && dif(e.data) <= 14);
  if (!prox.length) ol.append(el("li", "suave", "Nada nos próximos 14 dias."));
  for (const e of prox) {
    const li = comCor(el("li", dif(e.data) <= 3 ? "perto" : ""), e.d);
    const q = el("span", "quando mono"); q.append(el("b", "", curta(e.data)), el("span", "", ` ${e.hora}`));
    const o = el("div", "oque"); const t = el("span"); t.innerHTML = e.oque;
    o.append(el("span", "disc", nome(e.d)), t);
    li.append(q, o, el("span", "falta mono", falta(e.data)));
    ol.append(li);
  }
}

function tarefas(ul, feitasUl) {
  const feitas = new Set(ler(FEITAS, []));
  const minhas = ler(MINHAS, []);
  const todas = [...D.tarefas, ...minhas.map(m => ({ ...m, origem: "minha" }))]
    .sort((a, b) => (a.prazo || "9999").localeCompare(b.prazo || "9999"));
  ul.replaceChildren(); feitasUl.replaceChildren();
  let nFeitas = 0;
  for (const t of todas) {
    const feita = feitas.has(t.id);
    const li = comCor(el("li", (t.prazo && dif(t.prazo) < 0 && !feita) ? "atrasada" : ""), t.d);
    const cb = el("input"); cb.type = "checkbox"; cb.checked = feita; cb.id = "t-" + t.id;
    cb.addEventListener("change", () => {
      cb.checked ? feitas.add(t.id) : feitas.delete(t.id);
      guardar(FEITAS, [...feitas]); tarefas(ul, feitasUl);
    });
    const lab = el("label"); lab.htmlFor = cb.id;
    const txt = el("span"); txt.innerHTML = t.texto;
    if (t.href) { const a = el("a"); a.href = abs(t.href); a.append(txt); lab.append(a); } else lab.append(txt);
    const meta = el("span", "meta mono");
    if (t.d) meta.append(el("span", "disc", nome(t.d)));
    if (t.prazo) meta.append(el("span", "", `${curta(t.prazo)} · ${falta(t.prazo)}`));
    if (t.origem === "minha") {
      const x = el("button", "apagar", "apagar"); x.type = "button";
      x.addEventListener("click", () => { guardar(MINHAS, ler(MINHAS, []).filter(m => m.id !== t.id)); tarefas(ul, feitasUl); });
      meta.append(x);
    }
    li.append(cb, lab, meta);
    (feita ? feitasUl : ul).append(li);
    if (feita) nFeitas++;
  }
  if (!ul.children.length) ul.append(el("li", "suave", "Tudo feito."));
  feitasUl.closest("details").hidden = !nFeitas;
  feitasUl.closest("details").querySelector("summary").textContent = `Feitas (${nFeitas})`;
}

function chegou(ul) {
  ul.replaceChildren();
  if (!D.chegou.length) ul.append(el("li", "suave", "Nada nos últimos 7 dias."));
  for (const c of D.chegou) {
    const li = comCor(el("li"), c.d);
    const a = el(c.href ? "a" : "span"); if (c.href) a.href = abs(c.href);
    a.append(el("b", "", nome(c.d)), document.createTextNode(` · ${c.texto}`));
    li.append(el("span", "quando mono", curta(c.data)), a, el("span", "onde mono", c.onde));
    ul.append(li);
  }
}

function avisos(ul, n) {
  ul.replaceChildren();
  for (const a of D.avisos.slice(0, n)) {
    const li = comCor(el("li"), a.d);
    const t = el("span"); t.innerHTML = a.html;
    li.append(el("span", "disc", nome(a.d)), t);
    ul.append(li);
  }
}

function agendaCompleta(alvo) {
  alvo.replaceChildren();
  for (const [titulo, sel] of [["Próximas", D.agenda.filter(e => dif(e.data) >= 0)], ["Já passaram", D.agenda.filter(e => dif(e.data) < 0).reverse()]]) {
    if (!sel.length) continue;
    const sec = el("section", "seccao"); sec.append(el("h2", "", titulo));
    const ol = el("ol", "agenda" + (titulo === "Já passaram" ? " passadas" : ""));
    for (const e of sel) {
      const li = comCor(el("li"), e.d);
      const o = el("div", "oque"); const t = el("span"); t.innerHTML = e.oque;
      o.append(el("span", "disc", nome(e.d)), t);
      if (e.notas) { const n = el("p", "notas"); n.innerHTML = e.notas; o.append(n); }
      li.append(el("span", "quando mono", `${curta(e.data)} ${e.hora}`), o, el("span", "falta mono", falta(e.data)));
      ol.append(li);
    }
    sec.append(ol); alvo.append(sec);
  }
}

function preencher() {
  document.documentElement.classList.add("desbloqueado");
  const p = id => document.getElementById(id);
  if (p("p-agenda")) {
    agendaProxima(p("p-agenda"));
    tarefas(p("p-tarefas"), p("p-feitas"));
    chegou(p("p-chegou"));
    avisos(p("p-avisos"), 6);
    p("p-gerado").textContent = `dados de ${curta(D.gerado)}`;
  }
  if (p("p-notas")) notas(p("p-notas"), cores, D.notas || {});
  if (p("agenda-pagina")) agendaCompleta(p("agenda-pagina"));
  document.querySelectorAll("[data-info]").forEach(e => {
    const h = D.info[e.dataset.info];
    if (h) { e.innerHTML = h; e.closest("section")?.removeAttribute("hidden"); }
  });
}

function bloquear() {
  try { localStorage.removeItem(CHAVE); } catch (e) {}
  location.reload();
}

async function iniciar() {
  let enc;
  try { enc = await (await fetch(ENC, { cache: "no-cache" })).json(); } catch (e) { return; }
  const form = document.getElementById("desbloquear");
  const guardada = (() => { try { return localStorage.getItem(CHAVE); } catch (e) { return null; } })();
  if (guardada) {
    try { D = await decifra(b64(guardada), enc); return preencher(); }
    catch (e) { try { localStorage.removeItem(CHAVE); } catch (e2) {} }
  }
  document.documentElement.classList.add("bloqueado");
  if (!form) return;
  const erro = document.getElementById("pp-erro");
  form.addEventListener("submit", async ev => {
    ev.preventDefault();
    erro.hidden = true;
    const botao = form.querySelector("button"); botao.disabled = true; botao.textContent = "A abrir…";
    let raw = null;
    try {
      raw = await deriva(form.querySelector("#pp").value, enc);
      D = await decifra(raw, enc);
    } catch (e) {
      D = null; erro.textContent = "Palavra-passe errada."; erro.hidden = false;
    }
    botao.disabled = false; botao.textContent = "Abrir";
    if (!D) return;
    try { localStorage.setItem(CHAVE, btoa(String.fromCharCode(...raw))); } catch (e) {}
    document.documentElement.classList.remove("bloqueado");
    preencher();
  });
}

document.getElementById("bloquear")?.addEventListener("click", bloquear);
document.getElementById("p-nova")?.addEventListener("submit", ev => {
  ev.preventDefault();
  const [txt, prazo] = ev.target.querySelectorAll("input");
  if (!txt.value.trim()) return;
  const minhas = ler(MINHAS, []);
  minhas.push({ id: "m" + Date.now().toString(36), texto: txt.value.trim().replace(/[<>&]/g, c => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" })[c]), prazo: prazo.value || "", d: "" });
  guardar(MINHAS, minhas);
  txt.value = ""; prazo.value = "";
  if (D) tarefas(document.getElementById("p-tarefas"), document.getElementById("p-feitas"));
});
iniciar();
