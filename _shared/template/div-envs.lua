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
      -- o pandoc (smart) faz "--" em "–" no solucoes.lua; aqui lê-se o texto cru
      ex_num = ex_txt:gsub("%-%-%-", "—"):gsub("%-%-", "–"):gsub("%s+", "")
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
-- completo "Aula 7 --- Título". Disciplinas sem aulas numeradas (Tecnologias
-- Web, resumida a partir do site) usam "# Tema 3 --- Título" da mesma forma.
local function Header(el)
  if not v2 or el.level ~= 1 or not FORMAT:match("latex") then return nil end
  local txt = pandoc.utils.stringify(el)
  -- "Aulas 5--6": um só PDF com duas aulas (Lógica); o número fica "5–6"
  local rotulo, n = txt:match("^(%a+)%s+(%d+[^%s]*)%s*—")
  if not n or (rotulo ~= "Aula" and rotulo ~= "Aulas" and rotulo ~= "Tema") then return nil end
  -- tira "Aula"/"Tema", espaço, número, espaço, travessão e espaço do início
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
  return pandoc.RawBlock("latex", "\\clearpage\\def\\aulanum{" .. n .. "}\\def\\aularotulo{" .. rotulo .. "}" ..
    "\\section[" .. rotulo .. " " .. n .. " --- " .. titulo .. "]{" .. titulo .. "}" .. id)
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
  -- HTML (site): a caixa fica um <div class="caixa definicao"> com o rótulo
  -- e o título por cima; o CSS do site desenha-a.
  if FORMAT:match("html") then
    local rotulos = { definicao = "Definição", exemplo = "Exemplo", pratica = "Pratica agora" }
    local rotulo = rotulos[class]
    if rotulo then
      local cab = { pandoc.Span(rotulo, { class = "rotulo" }) }
      if title and title ~= "" then
        table.insert(cab, pandoc.Space())
        table.insert(cab, pandoc.Span(pandoc.utils.blocks_to_inlines(pandoc.read(title, "markdown").blocks), { class = "titulo" }))
      end
      table.insert(el.content, 1, pandoc.Div({ pandoc.Plain(cab) }, { class = "cab" }))
      el.classes:insert(1, "caixa")
      el.attributes["title"] = nil
    end
    return el
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

-- Altura aproximada de um bloco, em linhas de texto (para os títulos não
-- ficarem sozinhos no fundo da página quando o bloco seguinte é uma caixa,
-- tabela ou código que não se parte e passa inteiro para a página seguinte).
-- Carateres que o parágrafo ocupa impresso. Uma fórmula conta ~40% do seu
-- código TeX ("\not\models_v" ocupa 2 carateres, não 13) e uma fórmula em
-- destaque conta como 2,5 linhas; sem isto, em Lógica cada título reservava
-- espaço a mais e deixava meias páginas vazias.
local function comprimento(b)
  local n = 0
  b:walk({
    Str = function(s) n = n + (utf8.len(s.text) or #s.text) end,
    Space = function() n = n + 1 end,
    Code = function(c) n = n + #c.text end,
    Math = function(m)
      if m.mathtype == "DisplayMath" then n = n + 250
      else n = n + math.ceil(#m.text * 0.4) end
    end,
  })
  return n
end

local function linhas_bloco(b)
  local t = b.t
  if t == "Para" or t == "Plain" then
    return math.ceil(comprimento(b) / 100) + 0.4
  elseif t == "CodeBlock" then
    local _, n = b.text:gsub("\n", ""); return n + 2
  elseif t == "BulletList" or t == "OrderedList" then
    local n = 0.5
    for _, item in ipairs(b.content) do
      for _, x in ipairs(item) do n = n + linhas_bloco(x) end
    end
    return n
  elseif t == "Table" then return linhas_tabela(b)
  elseif t == "Div" then
    local n = 2
    for _, x in ipairs(b.content) do n = n + linhas_bloco(x) end
    return n
  elseif t == "Header" then return 2.5
  end
  return 3
end

-- Linhas a reservar antes do título blocos[i]: o título mais o bloco
-- seguinte, se este não se partir (caixa, tabela, código curto), ou o
-- início do parágrafo/lista, se se partir.
local function linhas_titulo(blocos, i)
  local prox = blocos[i + 1]
  if not prox then return 3 end
  if prox.t == "Header" then return 2.5 + linhas_titulo(blocos, i + 1) end
  local n = linhas_bloco(prox)
  local depois = blocos[i + 2]
  if prox.t == "Para" and n <= 3.5 and depois and
     (depois.t == "Div" or depois.t == "Table") then
    -- título + uma frase de introdução + caixa/tabela: reservar também a
    -- caixa, senão o título e a frase ficam sozinhos no fundo da página
    n = n + linhas_bloco(depois)
  elseif prox.t == "Para" or prox.t == "BulletList" or prox.t == "OrderedList" then
    n = math.min(n, 3)
  end
  -- imagens não têm altura conhecida aqui: reservar pelo menos meia página
  if prox.t == "Para" and #prox.content == 1 and prox.content[1].t == "Image" then n = 22 end
  return math.min(3 + n, 8)
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
  if not FORMAT:match("latex") then return nil end
  local out = {}
  for i, el in ipairs(doc.blocks) do
    if el.t == "Header" and el.level >= 2 then
      table.insert(out, needspace(math.ceil(linhas_titulo(doc.blocks, i))))
    elseif el.t == "Table" then
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
