-- Converte ::: nomedaclasse ... ::: (fenced divs) em \begin{nomedaclasse}...\end{nomedaclasse}
-- para que as caixas definidas em preamble.tex (definicao, exemplo, atencao, exame) funcionem.
-- Atributo opcional title="..." vira o argumento opcional da tcolorbox, ex:
--   ::: {.definicao title=" — Autómato finito"}
local solucoes = nil

local function Meta(m)
  if m.solucoes then solucoes = pandoc.utils.stringify(m.solucoes) end
end

local function Div(el)
  local class = el.classes[1]
  if class == nil then
    return nil
  end
  local title = el.attributes["title"]
  local startEnv
  if title then
    startEnv = "\\begin{" .. class .. "}[" .. title .. "]"
  else
    startEnv = "\\begin{" .. class .. "}"
  end
  local endEnv = "\\end{" .. class .. "}"
  -- caixas "Pratica agora": rodapé a apontar para o HTML de soluções
  if class == "pratica" and solucoes then
    table.insert(el.content, pandoc.Para({
      pandoc.Emph({pandoc.Str("Soluções, uma alínea de cada vez:"), pandoc.Space(),
        pandoc.Link(pandoc.Code(solucoes), solucoes)})
    }))
  end
  table.insert(el.content, 1, pandoc.RawBlock("latex", startEnv))
  table.insert(el.content, pandoc.RawBlock("latex", endEnv))
  return el.content
end

-- Meta primeiro (para saber o nome do ficheiro de soluções), depois as caixas.
return { {Meta = Meta}, {Div = Div} }
