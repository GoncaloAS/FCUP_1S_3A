{
-- Analisador sintático para a calculadora simples
module Parser where
import Lexer  
}

%name parse
%tokentype { Token }
%error { parseError }

%token

-- completar as definições de tokens

%%

-- completar as regras da gramática
-- tenha em atenção de implementar as regras de precedência
-- e associatividade entre operadores!

{
parseError :: [Token] -> a
parseError toks = error "parse error"  
}

