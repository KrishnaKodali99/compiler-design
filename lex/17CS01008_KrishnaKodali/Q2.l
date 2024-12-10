%{
    #include<stdio.h>
%}

space   [\t]
letter  [a-zA-Z]
digit [0-9]
digits ({digit}+)
number ({digits}(.{digits})?)
lod ({letter}|{digit})
id  ({letter}{lod}*)
relop [<|>|<=|>=|=|<>]

%%
[ ] {}
if    {return 4;}
else  {return 5;}
then  {return 6;}
{id}    {return 2;}
{number}    {return 1;}
{relop} {return 3;}
\n  {return 0;}
.   {return 7;}
%%

int yywrap(void){ return 1;}

int main(){
    int token;
    while((token = yylex()) != 0){
        if(token == 1){
            printf("(number, %s)\n", yytext);
        }
        else if(token == 2){
            printf("(id, %s)\n", yytext);
        }
        else if(token == 3){
            printf("(relop, %s)\n", yytext);
        }
        else if(token == 4){
            printf("(if, %s)\n", yytext);
        }
        else if(token == 5){
            printf("(else, %s)\n", yytext);
        }
        else if(token == 6){
            printf("(then, %s)\n", yytext);
        }
        else if(token == 7){
            printf("(unidentified, %s)\n", yytext);
        }
    }
    return 0;
}
