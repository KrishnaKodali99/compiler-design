%{
    #include<stdio.h>
    int count0 = 0, count1 = 0, k=0;
%}

%%
[0] {count0++; }
[1] {count1++;}
.   {k = 1;
    return 0;}
\n  {return 0;}
%%

int yywrap(void){return 1;}
int main(){
    yylex();
    if(count0%2 == 0 && count1%2 == 0 && k == 0){
        printf("Even no. of Ones and Zeroes\n");
        printf("Zeroes Count = %d\nOnes Count = %d\n", count0, count1);
    }
    else if(k == 0)
        printf("Not Even number of Zeroes or Ones\n");
    else
        printf("Invalid String, Please enter a binary string\n");
    return 0;
}