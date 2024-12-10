RE --> NFA

1) Run the file RE_NFA.cpp in any c++ compiler.

2) Applicable for any Alphabet set.

3) Some of the points to be taken care are:
   -> Mention the concatenation with '.' operator
   -> Enclose every concatenation in a parenthesis
   -> Enclose the complete Regular Expression with Parenthesis 

4) Format for the regular Expressions is as follows:
   -> Regular Expression for 0 : (0)
   -> Regular Expression for 1 : (1)
   -> Regular Expression for 0|1 [OR]: (0|1)
   -> Regular Expression for 01 [CONCATENATION]: (0.1)
   -> Regular Expression for 0* [KLEENE CLOSURE]: (0*) 

Examples for outputs of some Regular Expressions are as follows:

1) (a.b|c)*

   The NFA has the transitions :
   Q0 --> Q1 : Symbol - ^
   Q1 --> Q2 : Symbol - ^
   Q2 --> Q3 : Symbol - a
   Q3 --> Q8 : Symbol - ^
   Q1 --> Q4 : Symbol - ^
   Q4 --> Q5 : Symbol - b
   Q5 --> Q8 : Symbol - ^
   Q1 --> Q6 : Symbol - ^
   Q6 --> Q7 : Symbol - c
   Q7 --> Q8 : Symbol - ^
   Q8 --> Q9 : Symbol - ^
   Q8 --> Q1 : Symbol - ^
   Q0 --> Q9 : Symbol - ^
   The final state is Q9

2) (0+(1.0))

   The NFA has the transitions :
   Q0 --> Q1 : Symbol - 1
   Q1 --> Q2 : Symbol - ^
   Q2 --> Q3 : Symbol - 0
   The final state is Q3