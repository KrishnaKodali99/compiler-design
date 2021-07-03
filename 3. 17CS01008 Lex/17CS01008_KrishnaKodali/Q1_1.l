%{
	#include<stdio.h>
	int count = 0, k = 0;
%}

%%
[0]	{count++;}
[1] {}
.	{k = 1;
    return 0;}
\n	{return 0;}
%%

int yywrap(void) {return 1;}

int main(){
    yylex();
    if(count%2 == 0 && k==0){
        printf("Binary string has Even No. of Zeroes\n");
        printf("Zeroes count = %d\n", count);
    }
    else if(k == 0){
        printf("Binary string has Odd No. of Zeroes\n");
        printf("Zeroes count = %d\n", count);
    }
    else
        printf("Invalid String, Please enter a binary string\n");
    return 0;
}