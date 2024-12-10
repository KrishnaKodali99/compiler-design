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
relop [<|>|<=|>=|=|<>|==]
op  [+|-|*|%|^|!|/]
sep  [;|,|{|}|(|)]

%%
[ ]         {}
main      {return 1;}
int         {return 2;}
float       {return 2;}
long        {return 2;}
elif        {return 3;}
if          {return 3;}
else        {return 3;}
for         {return 4;}
while       {return 4;}
read        {return 5;}
print       {return 6;}
{id}        {return 7;}
{number}    {return 8;}
{relop}     {return 9;}
{op}        {return 10;}
{sep}       {return 11;}
\n          {}
.           {return (int)yytext[0]+11;}
%%

int yywrap(void){return 1;}

int main(){
    int token;
    yyin = fopen("inputfile", "r");
    while((token = yylex()) != 0){
        if(token == 1)  
            printf("(funtion, %s)\n", yytext);
        else if(token == 2)
            printf("(data type, %s)\n", yytext);
        else if(token == 3)
            printf("(conditions, %s)\n", yytext);
        else if(token == 4)
            printf("(loop, %s)\n", yytext);
        else if(token == 5)
            printf("(input, %s)\n", yytext);
        else if(token == 6)
            printf("(output, %s)\n", yytext);
        else if(token == 7)
            printf("(id, %s)\n", yytext);
        else if(token == 8)
            printf("(number, %s)\n", yytext);
        else if(token == 9)
            printf("(relational operator, %s)\n", yytext);
        else if(token == 10)
            printf("(arithmetic operator, %s)\n", yytext);
        else if(token == 11)
            printf("(seperators, %s)\n", yytext);
        else
            printf("(unidentified symbol, %s)\n", yytext);        
    }
    return 0;
}


