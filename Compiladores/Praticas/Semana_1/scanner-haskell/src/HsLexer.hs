{-
  Um analisador lexical simples em Haskell
-}
module Main where

import Data.Char (isDigit, isSpace, isAlpha, isAlphaNum)

-- Tipo algébrico para tokens;
-- alguns dos casos ainda não estão implementados
data Token = ID String       -- e.g. xy123
           | NUM Int         -- e.g. 123
           | REAL Float      -- e.g. 123.45
           | LPAREN          -- (
           | RPAREN          -- )
           | LBRACE          -- {
           | RBRACE          -- }
           | COMMA           -- ,
           | SEMICOLON       -- ;
           | IF              -- if
           | WHILE           -- while
           | FOR             -- for
           | INT             -- int
           | FLOAT           -- float
           deriving (Eq,Show)

--
-- transformar lista de carateres numa lista de tokens
--
lexer :: [Char] -> [Token]
lexer [] = []
lexer (',':xs) = COMMA : lexer xs
lexer ('(':xs) = LPAREN : lexer xs
lexer (')':xs) = RPAREN  : lexer xs
lexer (x:xs)
  | isSpace x = lexer xs        -- consumir carateres brancos
lexer (x:xs)  
  | isDigit x = NUM (read (x:xs')) : lexer xs''
  where xs' = takeWhile isDigit xs
        xs''= dropWhile isDigit xs
lexer (x:xs)        
  | isAlpha x = lexerText (x:xs') : lexer xs''
  where xs' = takeWhile isAlphaNum xs
        xs''= dropWhile isAlphaNum xs
lexer (x:_)       -- outros carateres: erro
  = error ("invalid character: " ++ show x)


-- função auxiliar para distinguir palavras reservadas de identificadores
lexerText :: String -> Token
lexerText "if" = IF
lexerText xs   = ID xs


-- ler toda a entrada e imprimir a lista de tokens
main :: IO ()
main = do
  txt <- getContents
  print (lexer txt)

  
