#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Enumeração para tipos de tokens;
   alguns dos tokens não estão ainda implementados
*/
typedef enum
{
  ID,
  NUM,
  REAL,
  SEMICOLON,
  COMMA,
  LPAREN,
  RPAREN,
  LBRACE,
  RBRACE,
  IF,
  INT,
  FLOAT,
  WHILE,
  FOR,
  END_OF_FILE
} TokenType;

/* União para os valores dos tokens ;
   alguns dos valores ainda não são usados
*/
typedef union
{
  int ival;       // valor inteiro (NUM)
  float fval;     // valor vírgula flutuante (REAL)
  char text[255]; // texto (ID)
} TokenValue;

/* obter o próximo token
 */
TokenType getToken(TokenValue *token_value)
{
  int c = getchar();

  // Salta espaços em branco e comentários, alternadamente, até sobrar um
  // carácter que pertence mesmo a um token a sério.
  for (;;)
  {
    while (isspace(c)) // consumir carateres brancos
      c = getchar();

    if (c != '/')
      break; // não é início de comentário -> pronto para o switch

    int next = getchar();

    if (next == '*')
    {
      // comentário /* ... */
      c = getchar();
      for (;;)
      {
        while (c != '*' && c != EOF)
          c = getchar();
        if (c == EOF)
        {
          fprintf(stderr, "comentário não fechado\n");
          exit(-1);
        }
        c = getchar(); // carácter logo a seguir ao '*'
        if (c == '/')
        {
          c = getchar(); // avançar para depois do comentário
          break;
        }
        // senão, este 'c' pode ser outro '*' (ex: "**/") -> o while de
        // fora volta a testá-lo, sem o perder
      }
    }
    else if (next == '/')
    {
      // comentário // até ao fim da linha
      c = next;
      while (c != '\n' && c != EOF)
        c = getchar();
    }
    else
    {
      // '/' sozinho, não é comentário -> devolve 'next' ao stream e sai
      ungetc(next, stdin);
      break;
    }
  }

  switch (c)
  {
  case '(':
    return LPAREN;

  case ')':
    return RPAREN;

  case ',':
    return COMMA;

  case ';':
    return SEMICOLON;

  case '{':
    return LBRACE;

  case '}':
    return RBRACE;

  case EOF:
    return END_OF_FILE;

  default:
    if (isdigit(c))
    {
      int val = 0; // acumulador do valor decimal
      float fval = 0.0;
      while (isdigit(c))
      {
        val = 10 * val + c - '0';
        c = getchar();
      }

      float divisor = 10.0;

      if (c == '.')
      {
        c = getchar();
        while (isdigit(c))
        {
          fval = fval + (c - '0') / divisor;
          c = getchar();
          divisor *= 10.0;
        }
        ungetc(c, stdin);
        token_value->fval = val + fval;
        return REAL;
      }

      ungetc(c, stdin);        // devolver o último carater
                               // que foi consumido a mais
      token_value->ival = val; // valor do token

      return NUM;
    }
    else if (isalpha(c) || c == '_')
    {
      int k = 0;
      while (isalpha(c) || isdigit(c) || c == '_')
      {
        if (k < sizeof(token_value->text) - 1)
        {
          token_value->text[k] = c;
          k++;
        }
        c = getchar();
      }
      ungetc(c, stdin);
      token_value->text[k++] = '\0'; // terminar a string
      if (strcmp(token_value->text, "if") == 0)
        return IF; // palavra reservada
      else if (strcmp(token_value->text, "for") == 0)
        return FOR; // palavra reservada
      else if (strcmp(token_value->text, "while") == 0)
        return WHILE; // palavra reservada
      else if (strcmp(token_value->text, "int") == 0)
        return INT; // palavra reservada
      else if (strcmp(token_value->text, "float") == 0)
        return FLOAT; // palavra reservada
      else
        return ID; // caso contrário: identificador
    }
    else
    {
      fprintf(stderr, "unexpected character: %c\n", c);
      exit(-1);
    }
  }
}

/* função auxiliar para imprimir um token
 */
void printToken(TokenType token_type, TokenValue *token_value)
{
  switch (token_type)
  {
  case NUM:
    printf("NUM(%d) ", token_value->ival);
    break;

  case REAL:
    printf("REAL(%f) ", token_value->fval);
    break;

  case ID:
    printf("ID(%s) ", token_value->text);
    break;

  case IF:
    printf("IF ");
    break;

  case FOR:
    printf("FOR ");
    break;

  case WHILE:
    printf("WHILE ");
    break;

  case INT:
    printf("INT ");
    break;

  case FLOAT:
    printf("FLOAT ");
    break;

  case SEMICOLON:
    printf("SEMICOLON ");
    break;

  case COMMA:
    printf("COMMA ");
    break;

  case LPAREN:
    printf("LPAREN ");
    break;

  case RPAREN:
    printf("RPAREN ");
    break;

  case LBRACE:
    printf("LBRACE ");
    break;

  case RBRACE:
    printf("RBRACE ");
    break;

  case END_OF_FILE:
    printf("END_OF_FILE ");
    break;
  }
}

/* ler toda a entrada e imprimir a lista de tokens
 */
int main(void)
{
  TokenValue tok_val;
  TokenType next = getToken(&tok_val); // obter o primeiro token

  while (next != END_OF_FILE)
  {                             // enquanto não chegou ao fim
    printToken(next, &tok_val); // imprimir e obter o próximo
    next = getToken(&tok_val);
  }
  printf("\n");
}
