%{
    #include<stdio.h>
    #include <math.h>
    #include<stdlib.h>
    void yyerror(const char* str);
    int count=0, error=1;

    extern int yylineno;

    int label = 0; 
    int else_reference = 0;
    int while_reference = 0;
    #include "lex.yy.c"
%}

%token AND ASSIGN COLON COMMA DEF DIV DOT ELSE END EQ EXITLOOP FLOAT FLOAT_CONST FORMAT FROM FUN GE GLOBAL GT IF INT LEFT_PAREN LEFT_SQ_BKT LE LT MINUS MOD MULT NE NOT NUL OR PLUS PRINT PRODUCT READ RETURN RETURNS RIGHT_PAREN RIGHT_SQ_BKT SEMICOLON SKIP STEP STRING TO WHILE

%left PLUS MINUS
%left MULT DIV MOD
%nonassoc UMINUS UPLUS 
%nonassoc DOT
%left AND OR
%nonassoc NOT
%left LEFT_SQ_BKT RIGHT_SQ_BKT
%left LEFT_PAREN RIGHT_PAREN
%nonassoc IFX
%nonassoc ELSE

%union
{ 	
	char val[100];
}
   
%type<val> exp relOP bExp
%token<val> ID INT_CONST

%start S

%%
S : prog {};

prog : GLOBAL stmtListO END {} ;

stmtListO: stmtList {}
		 |  {};

stmtList: stmtList SEMICOLON stmt {}
		| stmt {};

stmt: assignmentStmt {}
	|readStmt {}
	|printStmt {}
	|ifStmt {}
	|whileStmt {}
;

assignmentStmt
  : ID ASSIGN exp {printf(" %s = %s\n",$1,$3);}
  ;

readStmt
  : READ ID {printf(" T%d = Read %s\n",count++,$2);}
  ;

printStmt
  : PRINT ID {printf(" print %s\n",$2);}
  ;

ifStmt
  : IF bExp 
  {
    printf(" T%d = %s\n",count,$2);
    printf(" If ! (T%d) goto L%d\n",count,label);
    else_reference = label;
    count++;
    label++;
  }

  COLON stmtList elsePart END
  ;

elsePart
  : ELSE 
  {
    printf(" goto L%d\n",label);
    printf(" L%d : ",else_reference);
    else_reference--;
    label++;
  }

  stmtList {printf(" L%d : ",label-1);}

  | {printf(" L%d : ",label);}
  ;

whileStmt: WHILE {
		            printf(" L%d : ",label);
		            while_reference = label;
		            label++;
		          }
    bExp {  
    		printf(" If ! (%s) goto L%d\n",$3,while_reference+1); 
    		label++;
    	 }

    COLON stmtList {
            printf(" goto L%d\n",while_reference); 
            printf(" L%d : ",while_reference+1);
            while_reference--;
            while_reference--;
          }
    END;

bExp: bExp OR bExp 	{
					    printf(" T%d = %s or %s\n",count,$1,$3); 
					    sprintf($$, "T%d", count++);
				    }
	| bExp AND bExp {
					    printf(" T%d = %s and %s\n",count,$1,$3); 
					    sprintf($$, "T%d", count++);
				    }
	| NOT bExp 		{
					    printf(" T%d = ! %s\n",count,$2); 
					    sprintf($$, "T%d", count++);
				    }
	| LEFT_PAREN bExp RIGHT_PAREN 
					{
					    printf(" T%d = %s\n",count,$2); 
					    sprintf($$, "T%d", count++);
				    }
	| exp relOP exp {
					    printf(" T%d = %s %s %s\n",count,$1,$2,$3); 
					    sprintf($$, "T%d", count++);
				    };

relOP
  : EQ {strcpy($$, "==");}
  | LE {strcpy($$, "<=");}
  | LT {strcpy($$, "<");}
  | GE {strcpy($$, ">=");}
  | GT {strcpy($$, ">");}
  | NE {strcpy($$, "!=");}
  ;


exp : exp PLUS exp {
						printf(" T%d = %s + %s\n",count,$1,$3);
    					sprintf($$, "T%d",count++);
    			   }
	| exp MINUS exp {
						printf(" T%d = %s - %s\n",count,$1,$3);
    					sprintf($$, "T%d",count++);
    			   }
	| exp MULT exp {
						printf(" T%d = %s * %s\n",count,$1,$3);
    					sprintf($$, "T%d",count++);
    			   }
	| exp DIV exp {
						printf(" T%d = %s / %s\n",count,$1,$3);
    					sprintf($$, "T%d",count++);
    			   }
	| exp MOD exp  {
						printf("T%d = %s modulo %s\n",count,$1,$3);
    					sprintf($$, "T%d",count++);
    			   }
	| MINUS exp    {
						printf(" T%d = -%s\n",count,$2);
    					sprintf($$, "T%d",count++);
    			   }
	| PLUS exp {
						printf(" T%d = +%s\n",count,$2);
    					sprintf($$, "T%d",count++);
    			   }
	
	| LEFT_PAREN exp RIGHT_PAREN {
						printf(" T%d = %s\n",count,$2);
    					sprintf($$, "T%d",count++);
    			   }
	| ID 
	| INT_CONST 
;

%%

extern int yylex();
extern int yyparse();
extern int line_num;

int main() 
{ 
	extern FILE *yyin;  
	yyin = fopen("input.txt","r");
	yyparse(); 
	if(error==1) 
		printf("\nAbove is the 3-Address code for the Grammar. \n\n"); 

	return 0;
} 

void yyerror(const char *str) 
{ 
	fprintf(stderr, "Error at line %d: %s\n", line_num, str);
	error=0; 
} 