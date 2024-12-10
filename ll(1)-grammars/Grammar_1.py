import re
import operator 
from functools import reduce

NT, T = [], []
Parse_Table, Stack = [], ["$", "E"]

def row(nt):
    if(nt == "E"):
        return 0
    if(nt == "E'"):
        return 1
    if(nt == "T"):
        return 2
    if(nt == "T'"):
        return 3
    if(nt == "F"):
        return 4

def col(t):
    if(t == "id"):
        return 0
    if(t == "+"):
        return 1
    if(t == "*"):
        return 2
    if(t == "("):
        return 3
    if(t == ")"):
        return 4
    if(t == "$"):
        return 5
    
def PredictiveParsing(s, details):
    global Stack
    global NT
    global Parse_Table
    s.append("$")
    i = 0
    if(details == 1):
        print("Stack" + "   Remaining Input   " + "Input Consumed") 
    while(len(s) != 1 and i != len(s)):
        if(details == 1):
            print(Stack, s[i:], i)
        if(Stack[-1] == s[i]):
            i += 1
            Stack.pop()
        elif(Stack[-1] != s[i]):
            if(Stack[-1] not in NT):
                return -1
            r, c = row(Stack[-1]), col(s[i])
            P = Parse_Table[r][c]
            if(P == ''):
                return -1
            Stack.pop()
            for j in range(len(P)-1, -1, -1):
                if(P[j] != "\u03B5"):
                    Stack.append(P[j])
    return 1

if __name__ == "__main__":
    NT = ["E", "E'", "T", "T'", "F"]
    T = ['+', '*',  ')', '(']
    Parse_Table = [['' for j in range(6)] for i in range(5)]
    Parse_Table[0][0], Parse_Table[0][3] = ["T", "E'"], ["T", "E'"]
    Parse_Table[1][1], Parse_Table[1][4] = ["+", "T", "E'"], ["\u03B5"]
    Parse_Table[1][5], Parse_Table[2][0] = ["\u03B5"],["F", "T'"]
    Parse_Table[2][3], Parse_Table[3][1] = ["F", "T'"], ["\u03B5"]
    Parse_Table[3][2], Parse_Table[3][4] = ["*", "F", "T'"], ["\u03B5"]
    Parse_Table[3][5], Parse_Table[4][0] = ["\u03B5"], ["id"]
    Parse_Table[4][3] = ["(", "E", ")"]
    print("Enter the input string: ")
    s, k = input(), 0
    s1 = re.sub("[^a-zA-Z0-9]", ' ', s).split()
    i, j, S =0, 0, list()
    while(i < len(s)):
        if(j < len(s1) and s[i] == s1[j][0]):
            S.append("id")
            i += len(s1[j])
            j += 1
        else:
            S.append(s[i])
            i += 1
    print("To show Stack and Remaining input at each step Type 1, else 0")
    details = int(input())
    P = PredictiveParsing(S, details)
    if(P == 1):
        print("String is accepted by the Grammar")
    else:
        print("String is not accepted by the Grammar")
        
    
    
    