// Visualizador dentro do site: ver.html?f=ficheiros/<caminho>&d=<Disciplina>&t=<título>
// PDF -> páginas desenhadas com PDF.js (só as que estão perto do ecrã);
// código/texto -> <pre> com números de linha; o resto -> descarregar.
const PDFJS = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.4.168/";
const TEXTO = /\.(c|h|l|y|x|hs|java|py|txt|flex|bison|js|css|html|mdown|sh|json|xml|csv)$|(^|\/)(Makefile|README)$/i;

const q = new URLSearchParams(location.search);
const f = q.get("f") || "";
const disciplina = q.get("d") || "";
const titulo = q.get("t") || f.split("/").pop();
const ver = document.getElementById("ver");
const meta = document.getElementById("ver-meta");
const paginas = document.getElementById("ver-paginas");

function erro(msg) {
  ver.innerHTML = "";
  const p = document.createElement("p");
  p.className = "ver-erro";
  p.textContent = msg;
  ver.appendChild(p);
}

// só ficheiros publicados deste site (nada de URLs de fora)
const valido = /^ficheiros\/[^:?#]+$/.test(f) && !f.split("/").includes("..");
document.title = `${titulo} — FCUP · 3.º ano`;
document.getElementById("ver-titulo").textContent = titulo;
const voltar = document.getElementById("voltar");
if (/^[\w-]+$/.test(disciplina)) {
  voltar.href = `${disciplina}/index.html`;
  voltar.textContent = disciplina === "TecnologiasWeb" ? "Tecnologias Web" : disciplina;
  fetch(`${disciplina}/index.html`).then(r => r.text()).then(t => {
    const m = t.match(/<html[^>]*data-cor="(\d)"/);
    if (m) document.documentElement.dataset.cor = m[1];
    const h = t.match(/<h1>([^<]+)/);
    if (h) voltar.textContent = h[1].trim();
  }).catch(() => {});
}
const descarregar = document.getElementById("ver-descarregar");
descarregar.href = f;
descarregar.setAttribute("download", f.split("/").pop());
meta.textContent = f.replace(/^ficheiros\//, "");

if (!valido) {
  erro("Ficheiro inválido.");
  descarregar.hidden = true;
} else if (/\.pdf$/i.test(f)) {
  pdf();
} else if (TEXTO.test(f)) {
  texto();
} else {
  erro("Este tipo de ficheiro não abre no browser. Usa o botão Descarregar.");
}

async function texto() {
  const r = await fetch(f);
  if (!r.ok) return erro("Não encontrei o ficheiro.");
  const linhas = (await r.text()).replace(/\n$/, "").split("\n");
  const pre = document.createElement("pre");
  pre.className = "ver-codigo";
  linhas.forEach((l, i) => {
    const s = document.createElement("span");
    s.className = "l";
    s.dataset.n = i + 1;
    s.textContent = l + "\n";
    pre.appendChild(s);
  });
  ver.innerHTML = "";
  ver.appendChild(pre);
  paginas.textContent = `${linhas.length} linhas`;
}

async function pdf() {
  ver.innerHTML = '<p class="ver-erro">A carregar…</p>';
  let lib;
  try {
    lib = await import(PDFJS + "pdf.min.mjs");
  } catch (e) {
    return erro("Não consegui carregar o visualizador de PDF (sem internet?). Usa o botão Descarregar.");
  }
  lib.GlobalWorkerOptions.workerSrc = PDFJS + "pdf.worker.min.mjs";
  let doc;
  try {
    doc = await lib.getDocument(f).promise;
  } catch (e) {
    return erro("Não consegui abrir este PDF. Usa o botão Descarregar.");
  }
  ver.innerHTML = "";
  paginas.textContent = `${doc.numPages} páginas`;

  const inverter = document.getElementById("ver-inverter");
  inverter.hidden = false;
  let inv = false;
  try { inv = localStorage.getItem("ver-inverter") === "1"; } catch (e) {}
  const aplica = () => { ver.classList.toggle("invertido", inv); inverter.setAttribute("aria-pressed", inv); };
  aplica();
  inverter.addEventListener("click", () => {
    inv = !inv; aplica();
    try { localStorage.setItem("ver-inverter", inv ? "1" : "0"); } catch (e) {}
  });

  // tamanho de cada página antes de desenhar (para o scroll não saltar)
  const primeira = await doc.getPage(1);
  const v1 = primeira.getViewport({ scale: 1 });
  const caixas = [];
  for (let n = 1; n <= doc.numPages; n++) {
    const c = document.createElement("div");
    c.className = "ver-pagina";
    c.style.aspectRatio = `${v1.width} / ${v1.height}`;
    c.dataset.n = n;
    c.id = `p${n}`;
    ver.appendChild(c);
    caixas.push(c);
  }

  const feitas = new Set();
  async function desenha(c) {
    const n = +c.dataset.n;
    if (feitas.has(n)) return;
    feitas.add(n);
    const pg = await doc.getPage(n);
    const base = pg.getViewport({ scale: 1 });
    c.style.aspectRatio = `${base.width} / ${base.height}`;
    const escala = (c.clientWidth / base.width) * Math.min(window.devicePixelRatio || 1, 2);
    const vp = pg.getViewport({ scale: escala });
    const canvas = document.createElement("canvas");
    canvas.width = Math.floor(vp.width);
    canvas.height = Math.floor(vp.height);
    canvas.setAttribute("aria-label", `Página ${n}`);
    c.appendChild(canvas);
    await pg.render({ canvasContext: canvas.getContext("2d"), viewport: vp }).promise;
  }
  const obs = new IntersectionObserver(es => es.forEach(e => e.isIntersecting && desenha(e.target)),
    { rootMargin: "800px 0px" });
  caixas.forEach(c => obs.observe(c));

  // página atual na barra
  const atual = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) paginas.textContent = `${e.target.dataset.n} / ${doc.numPages}`;
  }), { rootMargin: "-45% 0px -45% 0px" });
  caixas.forEach(c => atual.observe(c));
  if (location.hash.match(/^#p\d+$/)) document.querySelector(location.hash)?.scrollIntoView();
}
