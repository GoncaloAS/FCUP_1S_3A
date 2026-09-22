%{
#include <stdio.h>
%}
%option noyywrap
alpha    [_a-zA-Z]
digit    [0-9]
%%
[ \t\n]+ { } 
"(" { printf("LPAREN "); }
")" { printf("RPAREN "); }
"," { printf("COMMA "); }
";" { printf("SEMICOLON "); }
"{" { printf("LBRACE "); }
"}" { printf("RBRACE "); }
"if" { printf("IF "); }
"while" { printf("WHILE "); }
"for" { printf("FOR "); }
"int" { printf("INT "); }
"float" { printf("FLOAT "); }
{alpha}({alpha}|{digit})* { printf("ID(%s) ", yytext); }
[0-9]+ { printf("NUM(%d) ", atoi(yytext)); }
[0-9]+"."[0-9]* { printf("REAL(%f) ", atof(yytext)); }
"//".* { }
"/*"([^*]|"*"+[^*/])*"*"+"/" { }
%%

int main(void) {
  yylex();
  printf("\n");
  return 0;
}
