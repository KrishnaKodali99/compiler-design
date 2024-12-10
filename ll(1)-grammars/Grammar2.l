%{
    #include<stdio.h>
    #include<string.h>
    char line[100000];
%}

op [-+*/]
relop [=|<|>]
sep [{|}|(|)|;]
digit [0-9]
ic ({digit}+)
fc ({ic}.{ic})
str ('a-zA-Z0-9')
letter  [a-zA-Z]
lod ({letter}|{digit})
id  ({letter}{lod}*)

%%
[ ]         {}
prog        {return 1;}
int         {return 1;}
float       {return 1;}
if          {return 1;}
else        {return 1;}
then        {return 1;}
and         {return 1;}
or          {return 1;}
not         {return 1;}
do          {return 1;}
while       {return 1;}
end         {return 1;}
print       {return 1;}
scan        {return 1;}
:=          {return 1;}
{id}        {return 2;}
{str}       {return 3;}
{ic}        {return 4;}
{fc}        {return 5;}
{relop}     {return 1;}
{op}        {return 1;}
{sep}       {return 1;}
\n          {}
.           {return 10;}
%%

int yywrap(void){return 1;}

int main(){
    int token;  FILE *f;
    yyin = fopen("SampleInput_G2.txt", "r");
    yyout = fopen("G2tokens.txt", "w");
    while((token = yylex()) != 0){
        if(token == 1){
            printf("%s\n", yytext);
            fprintf(yyout, "%s\n", yytext);
        }
        else if(token == 2){
            printf("id\n");
            fprintf(yyout, "id\n");
        }
        else if(token == 3){
            printf("str\n");
            fprintf(yyout, "str\n");
        }
        else if(token == 4){
            printf("ic\n");
            fprintf(yyout, "ic\n");
        }
        else if(token == 5){
            printf("fc\n");
            fprintf(yyout, "fc\n");
        }
    }
    return 0;
}