-- Deduções em notação de Fitch (dedução natural), para o PDF e o HTML de soluções.
--
-- No Markdown escreve-se um bloco de código com a classe "fitch":
--
--   ```{.fitch}
--   (p /\ q) \/ (q /\ r)
--   ---
--   |> p /\ q
--   |  q                 ; &E, 2
--   |> q /\ r
--   |  q                 ; &E, 4
--   q                    ; vE, 1, 2-3, 4-5
--   ```
--
-- - Cada "|" no início da linha é um nível de sub-dedução (além da principal).
-- - "|>" (ou "||>", ...) abre uma sub-dedução nova: a linha é a hipótese
--   (fica sublinhada e a barra começa um pouco abaixo, para separar caixas
--   seguidas ao mesmo nível, como nas duas da eliminação de \/).
-- - "---" sublinha a linha anterior (fim das premissas da dedução principal).
-- - Depois de ";" vem a justificação: regra abreviada + linhas.
--   &I &E vI vE ~I ~E FI FE ->I ->E R MT RA TE ~~I   ("2-3" vira "2--3")
--   1.ª ordem: AI AE EI EE (∀I ∀E ∃I ∃E) =I =E; fórmulas "forall x P(x)",
--   "exists y (f(y) = a)", "t != u", "phi[v/x]". "|> [v] ..." abre a caixa
--   da variável nova v (∃E: a linha é a hipótese; ∀I: a linha leva
--   justificação e não é hipótese). naolivre="psi:x" no bloco: x não é
--   livre em psi (para o verificador). "|> [u]" sozinho numa linha abre a
--   caixa de u na linha seguinte (ex. ∀I à volta de uma hipótese, ou ∀x∀y).
-- - Fórmulas em ASCII: /\  \/  ~  ->  <->  F  T, e letras gregas por extenso
--   (phi psi delta gamma theta), com índice opcional: delta1 -> \delta_1.
--   O mesmo texto é lido por _shared/tools/fitch_check.py, que verifica a
--   dedução regra a regra.
-- - Classe extra ".nocheck": o verificador ignora o bloco (deduções erradas
--   de propósito, ou dadas sem justificações para o leitor completar).

local GREGAS = { phi = "\\phi", psi = "\\psi", delta = "\\delta",
  gamma = "\\gamma", theta = "\\theta", alpha = "\\alpha", beta = "\\beta",
  sigma = "\\sigma" }

-- fórmula ASCII -> LaTeX (modo matemático)
local function formula_tex(s)
  local out = {}
  local i = 1
  local depois_quant = false
  local n = #s
  while i <= n do
    local c = s:sub(i, i)
    local two = s:sub(i, i + 1)
    local three = s:sub(i, i + 2)
    if three == "<->" then table.insert(out, "\\leftrightarrow "); i = i + 3
    elseif two == "->" then table.insert(out, "\\to "); i = i + 2
    elseif two == "/\\" then table.insert(out, "\\land "); i = i + 2
    elseif two == "\\/" then table.insert(out, "\\lor "); i = i + 2
    elseif two == "!=" then table.insert(out, "\\neq "); i = i + 2
    elseif c == "~" then table.insert(out, "\\neg "); i = i + 1
    elseif c:match("%a") then
      local w = s:match("^%a+", i)
      local d = s:match("^%d*", i + #w)
      local quant = depois_quant
      depois_quant = false
      if w == "forall" or w == "exists" then
        table.insert(out, "\\" .. w .. " ")
        depois_quant = true
      elseif quant then
        table.insert(out, w .. (d ~= "" and ("_" .. d) or "") .. "\\, ")
      elseif GREGAS[w] then
        table.insert(out, GREGAS[w] .. (d ~= "" and ("_" .. d) or "") .. " ")
      elseif w == "F" or w == "T" then
        table.insert(out, "\\mathbf{" .. w .. "}" .. d .. " ")
      elseif #w > 1 then
        table.insert(out, "\\mathit{" .. w .. "}" .. (d ~= "" and ("_" .. d) or "") .. " ")
      else
        table.insert(out, w .. (d ~= "" and ("_" .. d) or "") .. " ")
      end
      i = i + #w + #d
    else
      table.insert(out, c); i = i + 1
    end
  end
  return table.concat(out)
end

local REGRAS = {
  { "~~I", "\\neg\\neg", "I" }, { "->I", "\\to", "I" }, { "->E", "\\to", "E" },
  { "&I", "\\land", "I" }, { "&E", "\\land", "E" },
  { "vI", "\\lor", "I" }, { "vE", "\\lor", "E" },
  { "~I", "\\neg", "I" }, { "~E", "\\neg", "E" },
  { "AI", "\\forall", "I" }, { "AE", "\\forall", "E" },
  { "EI", "\\exists", "I" }, { "EE", "\\exists", "E" },
}
local REGRAS_HTML = { ["\\neg\\neg"] = "¬¬", ["\\to"] = "→", ["\\land"] = "∧",
  ["\\lor"] = "∨", ["\\neg"] = "¬",
  ["\\forall"] = "∀", ["\\exists"] = "∃" }

-- "&E, 2-3" -> {simbolo="\\land", letra="E", resto=", 2--3"} ou {texto=...}
local function regra(j)
  for _, r in ipairs(REGRAS) do
    if j:sub(1, #r[1]) == r[1] then
      return { simbolo = r[2], letra = r[3], resto = j:sub(#r[1] + 1) }
    end
  end
  local w = j:match("^[^%s,]+") or ""
  local resto = j:sub(#w + 1)
  if w == "FI" or w == "FE" then
    return { negrito = "F", letra = w:sub(2), resto = resto }
  end
  return { texto = w, resto = resto }
end

local function parse(texto)
  local linhas = {}
  local pend = {}
  for raw in (texto .. "\n"):gmatch("(.-)\n") do
    local s = raw:gsub("%s+$", "")
    if s:match("^%s*$") then goto continue end
    local barras = s:match("^[|%s]*")
    local nivel = select(2, barras:gsub("|", ""))
    local resto = s:sub(#barras + 1)
    if resto:match("^%-%-%-") then
      if #linhas > 0 then linhas[#linhas].sublinhado = true end
      goto continue
    end
    local nova = false
    if resto:sub(1, 1) == ">" then nova = true; resto = resto:sub(2) end
    local f, j = resto:match("^(.-)%s*;%s*(.*)$")
    if not f then f = resto; j = "" end
    f = f:gsub("^%s+", "")
    local var = f:match("^%[(%w+)%]")
    if var then f = f:sub(#var + 3):gsub("^%s+", "") end
    if var and f == "" and j == "" then
      -- "|> [v]" sozinho: a caixa de v abre na linha seguinte
      table.insert(pend, { nivel = nivel, var = var })
      goto continue
    end
    table.insert(linhas, { nivel = nivel, nova = nova, sublinhado = nova and j == "",
      formula = f, just = j, var = var, abre = pend })
    pend = {}
    ::continue::
  end
  return linhas
end

local function just_tex(j)
  if j == "" then return "" end
  local r = regra(j)
  local resto = r.resto:gsub("(%d)%-(%d)", "%1--%2")
  if r.simbolo then return "$" .. r.simbolo .. "$" .. r.letra .. resto end
  if r.negrito then return "\\textbf{" .. r.negrito .. "}\\," .. r.letra .. resto end
  return r.texto .. resto
end

local function just_html(j)
  if j == "" then return "" end
  local r = regra(j)
  local resto = r.resto:gsub("(%d)%-(%d)", "%1–%2")
  if r.simbolo then return REGRAS_HTML[r.simbolo] .. r.letra .. resto end
  if r.negrito then return "<b>" .. r.negrito .. "</b>&#8239;" .. r.letra .. resto end
  return r.texto .. resto
end

-- caixas que abrem nesta linha: níveis e prefixo com as variáveis novas
local function abre_info(l)
  local niveis, vars = {}, {}
  for _, p in ipairs(l.abre or {}) do
    niveis[p.nivel] = true
    table.insert(vars, "\\boxed{" .. p.var .. "}\\; ")
  end
  if l.nova then niveis[l.nivel] = true end
  if l.var then table.insert(vars, "\\boxed{" .. l.var .. "}\\; ") end
  return niveis, table.concat(vars)
end

local function latex(linhas)
  local t = { "\\begin{fitchproof}" }
  for i, l in ipairs(linhas) do
    local barras = {}
    local niveis, pref = abre_info(l)
    for d = 0, l.nivel do
      -- a barra de uma caixa que abre aqui começa mais abaixo
      if niveis[d] then
        table.insert(barras, "\\fitchbarstart")
      else
        table.insert(barras, "\\fitchbar")
      end
    end
    local f = "$" .. pref .. formula_tex(l.formula) .. "$"
    if l.sublinhado then f = "\\fitchhyp{" .. f .. "}" end
    table.insert(t, i .. " & " .. table.concat(barras) .. f .. " & " ..
      just_tex(l.just) .. " \\\\")
  end
  table.insert(t, "\\end{fitchproof}")
  return pandoc.RawBlock("latex", table.concat(t, "\n"))
end

local function html(linhas)
  local max = 0
  for _, l in ipairs(linhas) do if l.nivel > max then max = l.nivel end end
  local blocos = { pandoc.RawBlock("html", '<table class="fitch"><tbody>') }
  for i, l in ipairs(linhas) do
    local tr = { '<tr><td class="n">' .. i .. '</td>' }
    local niveis, pref = abre_info(l)
    for d = 0, l.nivel do
      local cls = niveis[d] and "b s" or "b"
      table.insert(tr, '<td class="' .. cls .. '"></td>')
    end
    local cls = l.sublinhado and ' class="f hyp"' or ' class="f"'
    table.insert(tr, '<td colspan="' .. (max - l.nivel + 1) .. '"' .. cls .. '><span>')
    local plain = pandoc.Plain({ pandoc.RawInline("html", table.concat(tr)),
      pandoc.Math("InlineMath", pref .. formula_tex(l.formula)),
      pandoc.RawInline("html", '</span></td><td class="j">' .. just_html(l.just) .. '</td></tr>') })
    table.insert(blocos, plain)
  end
  table.insert(blocos, pandoc.RawBlock("html", "</tbody></table>"))
  return blocos
end

function CodeBlock(el)
  if not el.classes:includes("fitch") then return nil end
  local linhas = parse(el.text)
  if FORMAT:match("latex") then return latex(linhas) end
  if FORMAT:match("html") then return html(linhas) end
  return nil
end
