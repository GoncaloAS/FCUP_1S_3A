/**
 * Smoke test: valida o banco de perguntas de Redes (redes.html).
 * Mesmo esquema do output.js: [topic, id, questionHtml, options(4), correctIdx(0-3), explanationHtml, hintHtml];
 * resposta aberta (desenvolvimento): [topic, id, enunciadoHtml, null, -1, resoluçãoHtml, notaHtml].
 * Verifica também que redes.html carrega todos os ficheiros do banco, que as âncoras do guia existem,
 * que cada explicação justifica a certa e as três erradas, e que a certa está equilibrada pelas letras.
 */
const fs = require('fs');
const path = require('path');
const assert = require('assert');

const ROOT = path.resolve(__dirname, '..', '..');
const DIR = path.join(ROOT, 'assets', 'js', 'data', 'questions-redes');
const files = fs.readdirSync(DIR).filter(f => f.endsWith('.js')).sort();
assert.ok(files.length > 0, 'Não encontrei ficheiros em questions-redes/');

const html = fs.readFileSync(path.join(ROOT, 'redes.html'), 'utf8');
files.forEach(f => assert.ok(html.includes(`questions-redes/${f}`), `redes.html não carrega ${f}`));

const bundle = files.map(f => fs.readFileSync(path.join(DIR, f), 'utf8')).join('\n') + '\n' +
  fs.readFileSync(path.join(ROOT, 'output-redes.js'), 'utf8') + '\n; return ALL;';
// eslint-disable-next-line no-new-func
const ALL = new Function(bundle)();
const guia = fs.readFileSync(path.join(ROOT, 'guia_redes_teste1.html'), 'utf8');

const ids = new Set();
const letras = [0, 0, 0, 0];
let abertas = 0;
ALL.forEach((q, i) => {
  assert.strictEqual(q.length, 7, `#${i}: ${q.length} campos`);
  const [topic, id, text, opts, ci, exp, hint] = q;
  assert.ok(topic && text && exp && hint, `#${i}: campo vazio`);
  assert.ok(!ids.has(id), `id repetido: ${id}`); ids.add(id);
  const ancora = hint.match(/guia_redes_teste1\.html#([^"]+)"/);
  assert.ok(ancora && guia.includes(`id="${ancora[1]}"`), `${id}: âncora do guia inexistente`);
  if (opts === null) {  // resposta aberta (desenvolvimento): resolução completa, figuras existentes
    abertas++;
    assert.strictEqual(ci, -1, `${id}: aberta com correctIdx`);
    assert.ok(exp.includes('class="sol-aberta"') && exp.length > 300, `${id}: resolução vazia`);
    (exp.match(/src="([^"]+)"/g) || []).forEach(s => {
      const f = s.slice(5, -1);
      assert.ok(fs.existsSync(path.join(ROOT, f)), `${id}: figura ${f} não existe`);
    });
    return;
  }
  assert.strictEqual(opts.length, 4, `${id}: opções`);
  assert.ok(ci >= 0 && ci <= 3, `${id}: correctIdx`);
  assert.ok(exp.includes(`(${'ABCD'[ci]}) Certa.`), `${id}: explicação não marca a certa`);
  ['A','B','C','D'].filter((_, k) => k !== ci).forEach(l =>
    assert.ok(exp.includes(`(${l}) Errada.`), `${id}: falta explicar porque é que a (${l}) está errada`));
  letras[ci]++;
});
assert.ok(abertas >= 30, `esperava as perguntas de desenvolvimento do teste modelo, encontrei ${abertas}`);

// a resposta certa tem de estar equilibrada pelas quatro letras
assert.ok(Math.max(...letras) - Math.min(...letras) <= 2, `posições da certa desequilibradas: ${letras}`);
