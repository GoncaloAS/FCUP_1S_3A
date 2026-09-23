-- Filtro pandoc para os documentos SOLUCOES_<Disciplina>.md -> .html
--
-- Convenção do Markdown:
--   ## Aula N --- título              (secção, aparece no índice)
--   ### 1.2 --- título do exercício   (enunciado visível, aparece no índice)
--   #### (a) enunciado da alínea      (vira uma alínea fechada: <details>)
--   ...conteúdo da solução...
--
-- Cada "####" e tudo o que vem a seguir, até ao próximo cabeçalho de nível
-- <= 4, fica escondido dentro de <details class="sol">. O id de cada alínea
-- é "<nº do exercício>-<alínea>" (ex: "1.2-a", "Ex.4-c"), para se poder abrir
-- diretamente com #id no URL; se se repetir, leva um sufixo "-2", "-3", ...

function Pandoc(doc)
  local out = {}
  local open = false
  local ex_num = "sol"
  local n = 0
  local seen = {}

  local function close()
    if open then
      table.insert(out, pandoc.RawBlock("html", "</div></details>"))
      open = false
    end
  end

  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level <= 4 then
      close()
    end
    if b.t == "Header" and b.level == 3 then
      -- "1.2 --- Traduzir..." -> "1.2"; "Ex. 4 --- ..." -> "Ex.4"
      local txt = pandoc.utils.stringify(b.content)
      ex_num = (txt:match("^(.-)%s+[-—]") or b.identifier):gsub("%s+", "")
      n = 0
      table.insert(out, b)
    elseif b.t == "Header" and b.level == 4 then
      n = n + 1
      local txt = pandoc.utils.stringify(b.content)
      local alinea = txt:match("^%((%w+)%)") or txt:match("^(%d+)%.") or tostring(n)
      local id = ex_num .. "-" .. alinea
      if seen[id] then
        seen[id] = seen[id] + 1
        id = id .. "-" .. seen[id]
      else
        seen[id] = 1
      end
      table.insert(out, pandoc.RawBlock("html",
        '<details class="sol" id="' .. id .. '"><summary>'))
      table.insert(out, pandoc.Plain(b.content))
      table.insert(out, pandoc.RawBlock("html", '</summary><div class="corpo">'))
      open = true
    else
      table.insert(out, b)
    end
  end
  close()

  doc.blocks = out
  return doc
end
