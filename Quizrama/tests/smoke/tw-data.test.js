/**
 * Smoke test: valida o banco de perguntas de Tecnologias Web (tw.html).
 * Esquema: [topic, id, questionHtml, options(4), correctIdx(0-3), explanationHtml, hintHtml].
 * Verifica que tw.html carrega todos os ficheiros do banco, que as âncoras do guia existem, que cada explicação
 * justifica a certa e as três erradas, que a certa está equilibrada pelas letras e que NÃO é
 * sistematicamente a opção mais comprida (o truque "escolhe a maior" não pode funcionar).
 */
const fs = require('fs');
const path = require('path');
const assert = require('assert');

const ROOT = path.resolve(__dirname, '..', '..');
const DIR = path.join(ROOT, 'assets', 'js', 'data', 'questions-tw');
const files = fs.readdirSync(DIR).filter(f => f.endsWith('.js')).sort();
assert.ok(files.length > 0, 'Não encontrei ficheiros em questions-tw/');

const html = fs.readFileSync(path.join(ROOT, 'tw.html'), 'utf8');
files.forEach(f => assert.ok(html.includes(`questions-tw/${f}`), `tw.html não carrega ${f}`));

const bundle = files.map(f => fs.readFileSync(path.join(DIR, f), 'utf8')).join('\n') + '\n' +
  fs.readFileSync(path.join(ROOT, 'output-tw.js'), 'utf8') + '\n; return ALL;';
// eslint-disable-next-line no-new-func
const ALL = new Function(bundle)();
const guia = fs.readFileSync(path.join(ROOT, 'guia_tw_teste1.html'), 'utf8');
const plano = s => s.replace(/<[^>]+>/g, '').replace(/&[a-z]+;/g, 'x');

const ids = new Set();
const letras = [0, 0, 0, 0];
let maior = 0;
ALL.forEach((q, i) => {
  assert.strictEqual(q.length, 7, `#${i}: ${q.length} campos`);
  const [topic, id, text, opts, ci, exp, hint] = q;
  assert.ok(topic && text && exp && hint, `#${i}: campo vazio`);
  assert.ok(!ids.has(id), `id repetido: ${id}`); ids.add(id);
  const ancora = hint.match(/guia_tw_teste1\.html#([^"]+)"/);
  assert.ok(ancora && guia.includes(`id="${ancora[1]}"`), `${id}: âncora do guia inexistente`);
  assert.strictEqual(opts.length, 4, `${id}: opções`);
  assert.ok(ci >= 0 && ci <= 3, `${id}: correctIdx`);
  assert.ok(exp.includes(`(${'ABCD'[ci]}) Certa.`), `${id}: explicação não marca a certa`);
  ['A', 'B', 'C', 'D'].filter((_, k) => k !== ci).forEach(l =>
    assert.ok(exp.includes(`(${l}) Errada.`), `${id}: falta explicar porque é que a (${l}) está errada`));
  opts.forEach(o => assert.ok(!/(todas|nenhuma) (as|das) anteriores/i.test(o), `${id}: opção que depende da posição`));
  const lens = opts.map(o => plano(o).length);
  if (lens[ci] > Math.max(...lens.filter((_, k) => k !== ci))) maior++;
  letras[ci]++;
});
assert.ok(ALL.length >= 120, `banco pequeno: ${ALL.length}`);
assert.ok(Math.max(...letras) - Math.min(...letras) <= 2, `posições da certa desequilibradas: ${letras}`);
assert.ok(maior / ALL.length <= 0.30, `a certa é a opção mais comprida em ${Math.round(100 * maior / ALL.length)}% das perguntas`);
