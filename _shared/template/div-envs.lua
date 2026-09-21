-- Converte ::: nomedaclasse ... ::: (fenced divs) em \begin{nomedaclasse}...\end{nomedaclasse}
-- para que as caixas definidas em preamble.tex (definicao, exemplo, atencao, exame) funcionem.
-- Atributo opcional title="..." vira o argumento opcional da tcolorbox, ex:
--   ::: {.definicao title=" — Autómato finito"}
function Div(el)
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
  table.insert(el.content, 1, pandoc.RawBlock("latex", startEnv))
  table.insert(el.content, pandoc.RawBlock("latex", endEnv))
  return el.content
end
