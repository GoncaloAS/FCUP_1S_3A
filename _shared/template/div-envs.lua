-- Converte ::: nomedaclasse ... ::: (fenced divs) em \begin{nomedaclasse}...\end{nomedaclasse}
-- para que as caixas definidas em preamble.tex (definicao, exemplo, atencao, exame) funcionem.
-- Atributo opcional title="..." vira o argumento opcional da tcolorbox, ex:
--   ::: {.definicao title=" — Autómato finito"}
local solucoes = nil
local v2 = false  -- estilo v2 (preamble-v2.tex), ligado com -M estilo=v2

-- Alíneas de cada secção "##" do SOLUCOES_<Disciplina>.md, pela ordem.
-- A k-ésima caixa "pratica" do resumo corresponde à k-ésima secção "##".
-- Os ids são calculados como no solucoes.lua (têm de dar o mesmo).
local grupos = nil
local n_pratica = 0

local function ler_solucoes(caminho, prefixo)
  local f = io.open(caminho, "r")
  if not f then return nil end
  local gs, atual, ex_num, ex_txt, n, seen = {}, nil, "sol", "", 0, {}
  for linha in f:lines() do
    local h2 = linha:match("^## (.*)")
    local h3 = linha:match("^### (.*)")
    local h4 = linha:match("^#### (.*)")
    if h2 then
      atual = {}; table.insert(gs, atual)
    elseif h3 then
      ex_txt = (h3:match("^(.-)%s+%-%-%-") or h3:match("^(.-)%s+—") or h3)
      ex_num = ex_txt:gsub("%s+", "")
      n = 0
    elseif h4 and atual then
      n = n + 1
      local alinea = h4:match("^%((%w+)%)") or h4:match("^(%d+)%.") or tostring(n)
      local id = prefixo .. ex_num .. "-" .. alinea
      if seen[id] then seen[id] = seen[id] + 1; id = id .. "-" .. seen[id]
      else seen[id] = 1 end
      local rotulo = ex_txt
      if h4:match("^%((%w+)%)") then rotulo = ex_txt .. " (" .. alinea .. ")"
      elseif h4:match("^(%d+)%.") then rotulo = ex_txt .. " " .. alinea .. "." end
      table.insert(atual, { id = id, rotulo = rotulo })
    end
  end
  f:close()
  return gs
end

local function Meta(m)
  if m.solucoes then solucoes = pandoc.utils.stringify(m.solucoes) end
  if m.estilo and pandoc.utils.stringify(m.estilo) == "v2" then v2 = true end
  if v2 and m.solucoes_md and solucoes then
    local pasta = solucoes:match("#(.+)$") or ""
    grupos = ler_solucoes(pandoc.utils.stringify(m.solucoes_md), pasta .. "-")
  end
end

-- v2: "# Aula 7 --- Título" -> número grande + título (ver \aulahead no
-- preamble-v2.tex). O índice e o cabeçalho das páginas ficam com o nome
-- completo "Aula 7 --- Título".
local function Header(el)
  if not v2 or el.level ~= 1 then return nil end
  local txt = pandoc.utils.stringify(el)
  local n = txt:match("^Aula%s+(%d+)%s*—")
  if not n then return nil end
  -- tira "Aula", espaço, número, espaço, travessão e espaço do início
  local inl = el.content
  while #inl > 0 do
    local first = inl[1]
    local done = first.t == "Str" and first.text == "—"
    table.remove(inl, 1)
    if done then break end
  end
  if #inl > 0 and inl[1].t == "Space" then table.remove(inl, 1) end
  local function tex(i)
    return pandoc.write(pandoc.Pandoc({pandoc.Plain(i)}), "latex"):gsub("%s+$", "")
  end
  local titulo = tex(inl)
  local id = el.identifier ~= "" and ("\\label{" .. el.identifier .. "}") or ""
  return pandoc.RawBlock("latex", "\\clearpage\\def\\aulanum{" .. n .. "}" ..
    "\\section[Aula " .. n .. " --- " .. titulo .. "]{" .. titulo .. "}" .. id)
end

local function Div(el)
  local class = el.classes[1]
  if class == nil then
    return nil
  end
  local title = el.attributes["title"]
  if v2 and title then
    -- o rótulo da caixa já separa o tipo do título: tira o "--- " inicial
    title = title:gsub("^%-%-%-%s*", ""):gsub("^—%s*", "")
  end
  local startEnv
  if title then
    startEnv = "\\begin{" .. class .. "}[" .. title .. "]"
  else
    startEnv = "\\begin{" .. class .. "}"
  end
  local endEnv = "\\end{" .. class .. "}"
  -- caixas "Pratica agora": rodapé a apontar para o site de soluções
  -- (solucoes = "../SOLUCOES.html#<Disciplina>"; mostra só o nome do ficheiro)
  if class == "pratica" and solucoes then
    n_pratica = n_pratica + 1
    local g = grupos and grupos[n_pratica]
    if g and #g > 0 then
      -- v2: uma ligação por alínea, que abre o site já nessa alínea
      local base = solucoes:match("^([^#]*)") or solucoes
      local ins = { pandoc.Str("Soluções:"), pandoc.Space() }
      for i, a in ipairs(g) do
        if i > 1 then table.insert(ins, pandoc.Str(",")); table.insert(ins, pandoc.Space()) end
        table.insert(ins, pandoc.Link(a.rotulo, base .. "#" .. a.id))
      end
      table.insert(el.content, pandoc.Para({ pandoc.Emph(ins) }))
    else
      local rotulo = solucoes:match("([^/#]+)#?[^/]*$") or solucoes
      local texto = v2 and "Soluções:" or "Soluções, uma alínea de cada vez:"
      table.insert(el.content, pandoc.Para({
        pandoc.Emph({pandoc.Str(texto), pandoc.Space(),
          pandoc.Link(pandoc.Code(rotulo), solucoes)})
      }))
    end
  end
  table.insert(el.content, 1, pandoc.RawBlock("latex", startEnv))
  table.insert(el.content, pandoc.RawBlock("latex", endEnv))
  return el.content
end

-- Meta primeiro (para saber o nome do ficheiro de soluções), depois as caixas.
-- v2: tabelas e blocos de código curtos nunca se partem entre duas páginas
-- ("não pode ficar texto a meio"): se não couberem no que resta da página,
-- passam inteiros para a seguinte. Código com mais de 20 linhas parte-se
-- (empurrá-lo inteiro deixava meias páginas vazias).
local function needspace(linhas)
  return pandoc.RawBlock("latex", "\\Needspace*{" .. linhas .. "\\baselineskip}")
end

local function linhas_tabela(el)
  local n = #el.head.rows + 2
  for _, b in ipairs(el.bodies) do n = n + #b.body end
  return math.floor(n * 1.15) + 1
end

-- Só no nível de topo: dentro das caixas (não-quebráveis) não é preciso.
local function Pandoc(doc)
  if not v2 then return nil end
  if grupos then
    local caixas = 0
    doc:walk({ Div = function(d) if d.classes[1] == "pratica" then caixas = caixas + 1 end end })
    if caixas ~= #grupos then
      io.stderr:write("AVISO: " .. caixas .. " caixas pratica no resumo, mas " .. #grupos ..
        " secções ## no SOLUCOES: as ligações das soluções ficam desalinhadas.\n")
    end
  end
  local out = {}
  for _, el in ipairs(doc.blocks) do
    if el.t == "Table" then
      local n = linhas_tabela(el)
      if n <= 40 then table.insert(out, needspace(n)) end
    elseif el.t == "CodeBlock" then
      local _, n = el.text:gsub("\n", "")
      if n + 2 <= 20 then table.insert(out, needspace(n + 2)) end
    end
    table.insert(out, el)
  end
  doc.blocks = out
  return doc
end

return { {Meta = Meta}, {Pandoc = Pandoc}, {Header = Header, Div = Div} }
