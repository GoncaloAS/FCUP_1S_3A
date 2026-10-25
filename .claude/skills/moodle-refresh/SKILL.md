---
name: moodle-refresh
description: Refresh semanal do Moodle (moodle2627.up.pt) de todas as disciplinas — vê o que é novo ou mudou desde o último refresh, traz os ficheiros que faltam para a pasta certa, passa páginas do Moodle (fichas, soluções, enunciados) a PDF, e guarda a informação que não é documento (testes, prazos, avisos, avaliação, grupos) no INFO_<D>.pdf de cada disciplina e na AGENDA.pdf da raiz. Usar quando o Gonçalo pede o refresh do Moodle, "vai ao Moodle", "o que há de novo", ou que tragas o material de uma disciplina.
---

# Refresh do Moodle

O Gonçalo autorizou: abrir o Moodle com a sessão dele no Chrome e **descarregar**
todo o material das UCs dele. Só se lê: nunca submeter, publicar, responder em
fóruns, escolher grupos nem carregar em «Marcar como concluída».

Peças (não as reescrevas, usa-as):
- `_shared/moodle.json`: as UCs (id do curso → pasta). UC nova: ver «Disciplina nova».
- `.claude/skills/moodle-refresh/ref/extrair.js` (funções no browser) e `ref/inventario.js`
  (o que é novo/mudou). O `moodle.py js` junta os dois, já com o estado conhecido.
- `_shared/template/moodle.py` (`js`, `arrumar`, `pdf`, `fechar`, `agenda`). Correr com
  `uv run -q --with reportlab --with pillow python -I _shared/template/moodle.py <cmd>`
  (`js` basta `python3 -I`).
- Estado por disciplina: `<D>/.fonte/moodle/estado.json` (assinatura de cada atividade).

## Passos (poucas chamadas: cada uma reenvia o contexto)

**1. Abrir.** Sem screenshots (só texto: JS + `get_page_text`). Um só `ToolSearch` com `tabs_context_mcp, tabs_create_mcp, navigate,
javascript_tool, get_page_text, browser_batch, tabs_close_mcp`. Separador novo em
`https://moodle2627.up.pt/my/courses.php`. Se aparecer o login, para e pede ao
Gonçalo para entrar (nunca escrevas credenciais).

**2. Inventário.** `python3 -I _shared/template/moodle.py js` e cola a saída **tal
e qual** no `javascript_tool`; no mesmo `browser_batch`, `get_page_text`. Sai, por
UC, só o que é `NOVO`/`MUDOU` (com a secção, o ficheiro do Moodle, datas, texto
das etiquetas e os títulos dos tópicos novos nos fóruns), e «ainda sem acesso»
(listado mas fechado). Não navegues mais nesse separador: as funções ficam em
`window` e tudo o resto é por `fetch`.

**3. Decidir o destino de cada linha** (relativo à pasta da disciplina; ver
também o `.fonte/CONTEXTO_<D>.md`):

| No Moodle | Vai para |
|---|---|
| slides de teórica | `Teoricas/Aula_NN.<ext>`, com NN = próximo número pela ordem em que as aulas foram dadas (como no `resumo-semanal`) |
| livro, notas, bibliografia, material suplementar | `Teoricas/Extra_<Nome>.pdf` + uma linha no `CONTEXTO_<D>` («suplementar») |
| ficha/handout em ficheiro | `Praticas/Semana_N/<nome do Moodle>` (N segue a numeração que já existe na disciplina) |
| `.zip` de prática | `Praticas/Semana_N/<nome>.zip` (o `arrumar` extrai-o para a pasta `<nome>/`) |
| ficha em **página** do Moodle | `pagina(D, cm, "Praticas/Semana_N/ficha_N_<tema>.pdf")`; soluções: `solucoes_ficha_N.pdf` |
| enunciado de trabalho (assign ou ficheiro) | `Trabalho/…` (assign: `pagina(D, cm, "Trabalho/enunciado_<x>.pdf", "assign")`) |
| teste-modelo / teste antigo | `Testes/Teste_Modelo_N.pdf` (+ `_resolucao.pdf`) ou `Testes/Teste_<id>.pdf` |
| código anexo a uma página (`anexos por trazer`) | `ficheiro(D, caminho, "<mesma pasta>/<nome>")` |
| etiqueta, resumo de secção, datas de assign, tópico novo de fórum, escolha de grupo | **não é ficheiro**: vai para o `INFO_<D>` (passo 5) |
| `sigarracourseinfo`, `summaries`, URLs | só no 1.º refresh da UC (avaliação, bibliografia → `INFO_<D>`) |

`MUDOU` num ficheiro = nova revisão no Moodle: traz para o mesmo destino; o
`arrumar` grava `<nome>.novo.<ext>` ao lado. Compara (`pdftotext` + `diff`) e, se
for mesmo uma versão nova, substitui o antigo e diz-lho (o resumo pode precisar
de atualização).

**4. Trazer, numa só chamada** `javascript_tool`: os `await recurso(...)`,
`pagina(...)` e `ficheiro(...)` todos, e no fim `await entregar()`. Sai **um só**
`~/Downloads/moodle__lote_<hora>.zip` (o inventário já pôs lá o estado). Depois
`moodle.py arrumar`: abre o lote, põe cada ficheiro no sítio, extrai os `.zip`,
passa as páginas a PDF (estilo das fichas, fonte em `<D>/.fonte/moodle/`) e guarda o
estado novo. Página que saiu mal: corrige o `.md` em `.fonte/moodle/` e
`moodle.py pdf <md> <pdf>`. Se o lote não chegar a `~/Downloads`, o Chrome tem as
transferências automáticas bloqueadas para o Moodle: pede ao Gonçalo para as
permitir (ícone na barra de endereço ou Definições › Privacidade › Definições de
sites › Transferências automáticas) e repete o `entregar()`. Não mexas tu nas
definições do Chrome.

**5. Informação (`.fonte/INFO_<D>.md` → `INFO_<D>.pdf`).** Para tópicos novos
de fórum: `await avisos([ids])` + `get_page_text`. Atualiza com `Edit`:
- `## Datas`: tabela `| AAAA-MM-DD | hora | o quê | notas |` (data ISO na 1.ª
  coluna: é daqui que sai a `AGENDA.pdf`). Testes (com matéria e sala), entregas,
  defesas, sessões extra. Data ainda por marcar: numa frase por baixo da tabela.
- `## Avaliação` (ficha da UC: fórmula, mínimos, recurso), `## Trabalho prático`
  (grupo do Gonçalo, feedback que o docente lhe deu), `## Aulas` (horários, salas,
  apoio), `## Avisos` (mais recente primeiro, uma linha cada, com data) e
  `## Por publicar no Moodle` (o «ainda sem acesso»).
- `## A fazer`: o que um aviso pede ao Gonçalo, `- [ ] AAAA-MM-DD texto` (sem data
  se não tiver prazo). Vira tarefa no painel do site; entregas e testes da agenda
  e as fichas novas já viram tarefas sozinhos.
- Mudar a data em «Atualizado a …». Sem palavras-passe nem *passcodes* (Zoom:
  «link no Moodle») e sem dados de outros alunos. O `INFO` não vai para o site
  dos colegas (`build_site.py` salta-o).

**6. Fechar.** `moodle.py fechar`: aplica o estado (só agora, para não perder o
que ficou a meio), gera os `INFO_<D>.pdf`, a `AGENDA.pdf` e o painel pessoal
cifrado do site (`_shared/site/pessoal.enc`: agenda, tarefas, o que chegou,
avisos, INFO; a palavra-passe vem do Keychain, serviço `fcup-site`), e avisa se
ficou algo em `~/Downloads`. Fecha o separador.
**Publicar** (o Gonçalo autorizou fazer sempre): `git add` só dos ficheiros
desta sessão, por caminho (outras sessões partilham a árvore), incluindo
`_shared/site/pessoal.enc` se o `fechar` o refez; commit curto em português, sem
Co-Authored-By; `git push`. O site atualiza em ~2 min. Os INFO, a AGENDA e o
feedback de IPM estão no `.gitignore`: nunca os forces (`git add -f`).

**7. Relatório ao Gonçalo**, por disciplina: o que entrou (com o caminho), o que
mudou, datas novas ou alteradas (sobretudo testes e entregas próximos), avisos e
o que ainda está fechado. Se entraram teóricas novas, sugere o `resumo-semanal`
dessa disciplina (não o corras sem ele pedir; é uma disciplina por sessão).

## Disciplina nova

Os ids saem no browser com:
`(await (await fetch('/lib/ajax/service.php?sesskey='+M.cfg.sesskey,{method:'POST',body:JSON.stringify([{index:0,methodname:'core_course_get_enrolled_courses_by_timeline_classification',args:{offset:0,limit:0,classification:'inprogress',sort:'fullname'}}])})).json())[0].data.courses.map(c=>c.id+' '+c.fullname)`.
Junta `{"id": …, "disciplina": "<Pasta>"}` ao `_shared/moodle.json`. Se a pasta não
existir, cria a estrutura do `CLAUDE.md`. No 1.º refresh tudo aparece como `NOVO`:
compara com o que já existe (nome e tamanho) e traz só o que falta.
Disciplina sem Moodle (Tecnologias Web): só entra na agenda, pela secção
`## Datas` do documento indicado em `"outras"`.
