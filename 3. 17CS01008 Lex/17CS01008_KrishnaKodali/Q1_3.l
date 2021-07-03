%{
    #include<stdio.h>
%}

%%
^(0|(1(01*0)*10*)+)  {printf("Divisible by 3\n");}
.*  {printf("Not Divisible by 3\n");
    return 1;}
\n  {return 0;}
%%

int yywrap(void){ return 1;}
int main(){
    yylex();
    return 0;
}