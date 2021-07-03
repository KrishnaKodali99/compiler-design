%{ 
	#include<stdio.h>
    #include<stdlib.h>
    int error = 1;
    void yyerror();
%} 

%token NUMBER 

%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%% 
Expr: E{ 
        printf("\nResult = %d\n", $$); 
        return 0; 
        }; 
 E:E'+'E {$$=$1+$3;} 
  |E'-'E {$$=$1-$3;} 
  |E'*'E {$$=$1*$3;} 
  |E'/'E {$$=$1/$3;} 
  |E'%'E {$$=$1%$3;} 
  |'('E')' {$$=$2;} 
  | NUMBER {$$=$1;}; 
%% 

extern int yylex();
extern int yyparse();

void main() { 
	printf("\nEnter Any Expression: \n"); 
	yyparse(); 
} 

void yyerror() { 
	printf("\nEntered Expression is Invalid\n\n"); 
	error = 1; 
} 
