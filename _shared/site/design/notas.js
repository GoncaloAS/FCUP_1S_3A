// Notas do Gonçalo: uma linha por componente de avaliação de cada disciplina, guardadas só neste
// browser (localStorage "painel-notas"); nada vai para o repositório, que é público.
// Para cada disciplina: nota até agora, nota final (quando está tudo) e quanto falta para 9,5,
// respeitando os mínimos. As regras vêm das fichas das UC e dos slides de apresentação
// (ver o "## Avaliação" de cada <D>/.fonte/INFO_<D>.md). Mudou uma regra? Muda aqui também.
const OBJETIVO = 9.5, GUARDA = "painel-notas";

// max = escala em que se escreve a nota; vale = quanto pesa na nota final (em valores, de 20)
const REGRAS = [
  { d: "Compiladores", nome: "Compiladores", regra: "15% projeto 1 + 15% projeto 2 + 70% exame; mínimo 40% no exame.",
    comp: [{ id: "p1", n: "Projeto, 1.ª fase", max: 20, vale: 3 },
           { id: "p2", n: "Projeto, 2.ª fase", max: 20, vale: 3 },
           { id: "ex", n: "Exame", max: 20, vale: 14, min: 8 }] },
  { d: "IPM", nome: "Interação Pessoa-Máquina", regra: "1.º relatório 4 + 2.º relatório e apresentação 6 + exame 10 (mínimo 3,5 no exame).",
    comp: [{ id: "r1", n: "1.º relatório", max: 4, vale: 4 },
           { id: "r2", n: "2.º relatório + apresentação", max: 6, vale: 6 },
           { id: "ex", n: "Exame", max: 10, vale: 10, min: 3.5 }] },
  { d: "Logica", nome: "Lógica Computacional", regra: "50% 1.º teste + 50% 2.º teste; mínimo 6 em cada teste.",
    comp: [{ id: "t1", n: "1.º teste", max: 20, vale: 10, min: 6 },
           { id: "t2", n: "2.º teste", max: 20, vale: 10, min: 6 }] },
  { d: "Redes", nome: "Redes de Comunicação", regra: "3 testes de 30% + trabalho de programação 10%.",
    comp: [{ id: "t1", n: "1.º teste", max: 20, vale: 6 },
           { id: "t2", n: "2.º teste", max: 20, vale: 6 },
           { id: "t3", n: "3.º teste", max: 20, vale: 6 },
           { id: "tp", n: "Trabalho (chat)", max: 20, vale: 2 }] },
  { d: "TecnologiasWeb", nome: "Tecnologias Web", regra: "1.ª entrega 3 + 1.º teste 4 + 2.ª entrega 5 + 2.º teste 8. Frequência: ≥ 25% nos testes (3 de 12) e nas entregas (2 de 8).",
    comp: [{ id: "e1", n: "1.ª entrega", max: 3, vale: 3 },
           { id: "t1", n: "1.º teste", max: 4, vale: 4 },
           { id: "e2", n: "2.ª entrega", max: 5, vale: 5 },
           { id: "t2", n: "2.º teste", max: 8, vale: 8 }],
    grupos: [{ n: "testes", ids: ["t1", "t2"], min: 3 }, { n: "entregas", ids: ["e1", "e2"], min: 2 }] },
];

const ler = () => { try { return JSON.parse(localStorage.getItem(GUARDA)) || {}; } catch (e) { return {}; } };
const guardar = v => { try { localStorage.setItem(GUARDA, JSON.stringify(v)); } catch (e) {} };
const num = v => { if (v == null || v === "") return null; const x = parseFloat(String(v).replace(",", ".")); return isNaN(x) ? null : x; };
const fmt = x => (Math.round(x * 100) / 100).toLocaleString("pt-PT", { maximumFractionDigits: 2 });
const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; };

// estado de uma disciplina a partir das notas escritas
function avaliar(r, notas) {
  let feito = 0, falta = [], chumbo = [];
  for (const c of r.comp) {
    const v = notas[c.id];
    if (v == null) { falta.push(c); continue; }
    feito += v / c.max * c.vale;
    if (c.min != null && v < c.min) chumbo.push(`${c.n} abaixo do mínimo (${fmt(c.min)})`);
  }
  for (const g of r.grupos || []) {
    const soma = g.ids.reduce((s, id) => s + (notas[id] ?? 0), 0);
    const todos = g.ids.every(id => notas[id] != null);
    if (todos && soma < g.min) chumbo.push(`${g.n} abaixo de ${fmt(g.min)} (frequência)`);
  }
  if (!falta.length) {
    const ok = feito >= OBJETIVO && !chumbo.length;
    return { feito, final: true, ok, txt: ok ? `Final ${fmt(feito)}: passaste.` : `Final ${fmt(feito)}${chumbo.length ? " · " + chumbo.join("; ") : ""}.` };
  }
  // fração uniforme do máximo que falta, e o mínimo de cada componente por fazer
  const resto = falta.reduce((s, c) => s + c.vale, 0);
  const frac = Math.max(0, (OBJETIVO - feito) / resto);
  if (chumbo.length) return { feito, ok: false, txt: chumbo.join("; ") + "." };
  if (frac > 1) return { feito, ok: false, txt: `Mesmo com tudo no máximo não chegas a ${fmt(OBJETIVO)}: só recurso.` };
  const precisa = falta.map(c => `${c.n} ≥ ${fmt(Math.max(frac * c.max, c.min ?? 0))}/${fmt(c.max)}`);
  return { feito, ok: true, txt: `Para ${fmt(OBJETIVO)}: ${precisa.join(" · ")}` };
}

// base = notas que vêm do painel cifrado (secção "## Notas" do INFO_<D>.md); o que se escreve aqui por cima
// fica no localStorage e ganha (apagar um campo grava null: a nota do painel deixa de contar).
export function notas(alvo, cores = {}, base = {}) {
  const locais = ler(), todas = {};
  for (const r of REGRAS) {
    todas[r.d] = { ...(base[r.d] || {}) };
    for (const [k, v] of Object.entries(locais[r.d] || {})) { if (v == null) delete todas[r.d][k]; else todas[r.d][k] = v; }
  }
  alvo.replaceChildren();
  for (const r of REGRAS) {
    const minhas = todas[r.d] || {};
    const cart = el("div", "nota-uc");
    if (cores[r.d] != null) cart.dataset.cor = cores[r.d];
    const cab = el("div", "nota-cab");
    cab.append(el("b", null, r.nome));
    const tot = el("span", "nota-tot mono");
    cab.append(tot);
    cart.append(cab, el("p", "nota-regra suave", r.regra));
    const linhas = el("div", "nota-linhas");
    const estado = el("p", "nota-estado");
    const atualizar = () => {
      const e = avaliar(r, todas[r.d] || {});
      tot.textContent = `${fmt(e.feito)}/20${e.final ? "" : " até agora"}`;
      estado.textContent = e.txt;
      estado.className = "nota-estado " + (e.ok ? "ok" : "risco");
    };
    for (const c of r.comp) {
      const lab = el("label", "nota-linha");
      lab.append(el("span", null, c.n + (c.min != null ? ` (mín. ${fmt(c.min)})` : "")));
      const inp = el("input");
      Object.assign(inp, { type: "text", inputMode: "decimal", placeholder: "—", value: minhas[c.id] != null ? String(minhas[c.id]).replace(".", ",") : "" });
      inp.setAttribute("aria-label", `${r.nome}: ${c.n}`);
      const esc = el("span", "suave mono", `/${fmt(c.max)} · vale ${fmt(c.vale)}`);
      inp.addEventListener("input", () => {
        const v = num(inp.value);
        const ok = v == null || (v >= 0 && v <= c.max);
        inp.classList.toggle("invalida", !ok);
        if (!ok) return;
        if (v == null) delete todas[r.d][c.id]; else todas[r.d][c.id] = v;
        locais[r.d] = locais[r.d] || {}; locais[r.d][c.id] = v;
        guardar(locais);
        atualizar();
      });
      lab.append(inp, esc);
      linhas.append(lab);
    }
    cart.append(linhas, estado);
    alvo.append(cart);
    atualizar();
  }
}
