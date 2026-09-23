-- Alinhamento automático das colunas das tabelas (PDF e HTML de soluções).
--
-- Uma coluna sem alinhamento explícito (separador "|---|") é CENTRADA se
-- todas as células do corpo forem curtas: V/F, números, símbolos, fórmulas
-- curtas. Tabelas de verdade com os valores encostados à esquerda ficam
-- visualmente desligadas da fórmula no cabeçalho. Colunas com texto
-- comprido continuam à esquerda. A 1.ª coluna costuma ser de rótulos
-- ("LAN", "Texto simples"): só é centrada se tiver valores (V/F, números,
-- fórmulas), não palavras. Alinhamentos escritos à mão (":--", ":-:",
-- "--:") são sempre respeitados.

local LIMITE = 14 -- nº máximo de "caracteres visíveis" para contar como curta

-- comprimento aproximado do que se vê: em matemática, "\land" vale 1 carácter
local function visivel(inlines)
  local n = 0
  pandoc.walk_inline(pandoc.Span(inlines), {
    Str = function(s) n = n + utf8.len(s.text) end,
    Space = function() n = n + 1 end,
    Code = function(c) n = n + utf8.len(c.text) end,
    Math = function(m)
      local t = m.text:gsub("\\text%{([^}]*)%}", "%1")
                      :gsub("\\[a-zA-Z]+", "x")
                      :gsub("[{}%s]", "")
                      :gsub("[_^]", "")
      n = n + utf8.len(t)
    end,
  })
  return n
end

-- célula que é um "valor": só matemática, números, V/F ou símbolos soltos
local function valor(cell)
  local ok = true
  for _, b in ipairs(cell.contents) do
    if b.t ~= "Plain" and b.t ~= "Para" then return false end
    pandoc.walk_block(b, {
      Str = function(s)
        if s.text:match("%a%a") and not s.text:match("^[%d%p]+$") then ok = false end
      end,
      Code = function() ok = false end,
    })
  end
  return ok
end

local function curta(cell)
  local n = 0
  for _, b in ipairs(cell.contents) do
    if b.t == "Plain" or b.t == "Para" then
      n = n + visivel(b.content)
    else
      return false -- listas, blocos de código, etc.
    end
  end
  return n <= LIMITE
end

function Table(tbl)
  local ncols = #tbl.colspecs
  local tudo_curto = true -- todas as células do corpo curtas?
  for c = 1, ncols do
    local spec = tbl.colspecs[c]
    local todas, alguma, curtas = true, false, true
    for _, body in ipairs(tbl.bodies) do
      for _, row in ipairs(body.body) do
        local cell = row.cells[c]
        if cell then
          alguma = true
          local k = curta(cell)
          if not k then curtas = false end
          if not k or (c == 1 and not valor(cell)) then todas = false end
        end
      end
    end
    if not curtas then tudo_curto = false end
    if spec[1] == "AlignDefault" and alguma and todas then
      tbl.colspecs[c] = { "AlignCenter", spec[2] }
    end
  end
  -- Tabela só de valores curtos (ex: tabela de verdade): largura natural das
  -- colunas. Sem isto, uma linha comprida no .md faz o pandoc esticar a
  -- tabela à largura da página e partir os cabeçalhos em várias linhas.
  if tudo_curto then
    for c = 1, ncols do
      tbl.colspecs[c] = { tbl.colspecs[c][1], pandoc.ColWidthDefault }
    end
  end
  return tbl
end
