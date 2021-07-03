%{
    #include<stdio.h>
    #include<stdlib.h>
    #include"y.tab.h"
    extern int yylval;
%}

digit [0-9]
ic ({digit}+)
num {ic}?(.{ic})

%%
{ic}  { 
		yylval=atoi(yytext); 
		return NUMBER; 
	   }
[\n] return 0; 
. return yytext[0]; 
%%

int yywrap() { 
    return 1; 
}