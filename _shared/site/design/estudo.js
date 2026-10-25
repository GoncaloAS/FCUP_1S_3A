// Estudo: estudo.html?f=ficheiros/<ficha.pdf>&d=<Disciplina>&t=<título>&so=<prefixo das soluções>
// À esquerda o PDF (ver.html embutido), à direita as soluções dessa ficha (solucoes/ embutido).
// "lê a teoria" numa solução troca o PDF da esquerda para o resumo na página certa.
const q = new URLSearchParams(location.search);
const f = q.get("f") || "", d = q.get("d") || "", t = q.get("t") || f.split("/").pop(), so = q.get("so") || "";
const esq = document.getElementById("estudo-esq"), dir = document.getElementById("estudo-dir");
const voltarFicha = document.getElementById("estudo-ficha");
const valido = /^ficheiros\/[^:?#]+$/.test(f) && !f.split("/").includes("..") && /^[\w-]*$/.test(d);

const embute = href => { const u = new URL(href, location.href); u.searchParams.set("embed", "1"); return u.href; };
const ficha = embute(`ver.html?f=${encodeURIComponent(f)}&d=${encodeURIComponent(d)}&t=${encodeURIComponent(t)}`);

document.title = `${t} — estudo`;
document.getElementById("estudo-titulo").textContent = t;
const voltar = document.getElementById("estudo-voltar");
if (d) { voltar.href = `${d}/index.html`; voltar.textContent = d === "TecnologiasWeb" ? "Tecnologias Web" : d; }

// Modos: só o PDF (por omissão), lado a lado, ou só as soluções. As soluções só carregam quando são precisas.
const estudo = document.querySelector(".estudo"), modos = document.getElementById("estudo-modos");
function modo(m) {
  estudo.dataset.modo = m;
  modos.querySelectorAll("button").forEach(b => b.setAttribute("aria-pressed", b.dataset.modo === m));
  if (m !== "pdf" && !dir.src) dir.src = `solucoes/index.html?embed=1&so=${encodeURIComponent(so)}#${encodeURIComponent(d)}`;
}
modos.addEventListener("click", e => { const b = e.target.closest("button[data-modo]"); if (b) modo(b.dataset.modo); });

if (valido) {
  esq.src = ficha;
  if (so) modos.hidden = false;
} else {
  esq.replaceWith(Object.assign(document.createElement("p"), { className: "ver-erro", textContent: "Ficheiro inválido." }));
}

window.addEventListener("message", e => {
  if (e.origin !== location.origin || !e.data || typeof e.data.teoria !== "string") return;
  const u = new URL(e.data.teoria, location.href);
  if (u.origin !== location.origin || !u.pathname.endsWith("/ver.html")) return;
  esq.src = embute(u.href);
  voltarFicha.hidden = false;
  if (estudo.dataset.modo === "sol") modo("lado");  // o resumo tem de se ver
});
voltarFicha.addEventListener("click", () => { esq.src = ficha; voltarFicha.hidden = true; });
