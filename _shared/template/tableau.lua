-- Tableaux semânticos e refutações por resolução, desenhados com graphviz.
--
--   ```{.tableau seq="phi"}        ```{.resolucao de="phi"}
--   ~phi                            {~p, q}
--   ...                             ...
--   ```                             ```
--
-- A sintaxe e a verificação estão em _shared/tools/tableau.py, que também
-- gera o .dot (e escreve AVISOs no stderr se o bloco estiver errado).
-- PDF: figuras/auto/<sha1>.pdf (relativo à pasta da disciplina, onde o
-- tectonic procura). HTML: SVG embutido.
-- Atributo opcional escala="0.8" (só PDF; por defeito 0.8).

local DIR = pandoc.path.directory(PANDOC_SCRIPT_FILE)
local SCRIPT = pandoc.path.join({ DIR, "..", "tools", "tableau.py" })

local function pasta_disciplina()
  local f = PANDOC_STATE.input_files[1]
  return pandoc.path.directory(pandoc.path.directory(f))
end

function CodeBlock(el)
  local tipo
  if el.classes:includes("tableau") then tipo = "tableau"
  elseif el.classes:includes("resolucao") then tipo = "resolucao"
  else return nil end
  local attr = el.attributes.seq or el.attributes.de or ""
  local aberto = el.classes:includes("aberto") and "aberto" or ""
  local dot = pandoc.pipe("python3", { SCRIPT, "dot", tipo, attr, aberto }, el.text)
  if FORMAT:match("html") then
    local svg = pandoc.pipe("dot", { "-Tsvg" }, dot)
    svg = svg:gsub("^.-(<svg)", "%1")
    return pandoc.RawBlock("html", '<div class="arvore">' .. svg .. "</div>")
  end
  if FORMAT:match("latex") then
    local rel = "figuras/auto/" .. pandoc.sha1(tipo .. attr .. el.text) .. ".pdf"
    local base = pasta_disciplina()
    pandoc.system.make_directory(pandoc.path.join({ base, "figuras", "auto" }), true)
    local pdf = pandoc.pipe("dot", { "-Tpdf" }, dot)
    local fh = io.open(pandoc.path.join({ base, rel }), "wb")
    fh:write(pdf)
    fh:close()
    local escala = el.attributes.escala or "0.8"
    return pandoc.RawBlock("latex", "\\begin{center}\\includegraphics[scale="
      .. escala .. "]{" .. rel .. "}\\end{center}")
  end
  return nil
end
