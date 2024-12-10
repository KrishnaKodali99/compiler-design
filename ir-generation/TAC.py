import re
import pandas as pd

val, Nd, tac, result = 0, {}, dict(), dict()

def TAC(TC, I):
    global tac, val, result
    if(I == 1):
        tac["T"+str(val)] = TC[-2] + " + " + TC[-1]
        if("T" in TC[-2]):
            TC[-2] = result[TC[-2]]
        if("T" in TC[-1]):
            TC[-1] = result[TC[-1]]
        result["T"+str(val)] = float(TC[-2]) + float(TC[-1])
        TC.pop()
        TC.pop()
        TC.append("T"+str(val))
        val += 1
    if(I == 2):
        tac["T"+str(val)] = TC[-2] + " - " + TC[-1]
        if("T" in TC[-2]):
            TC[-2] = result[TC[-2]]
        if("T" in TC[-1]):
            TC[-1] = result[TC[-1]]
        result["T"+str(val)] = float(TC[-2]) - float(TC[-1])
        TC.pop()
        TC.pop()
        TC.append("T"+str(val))
        val += 1
    if(I == 4):
        tac["T"+str(val)] = TC[-2] + " * " + TC[-1]
        if("T" in TC[-2]):
            TC[-2] = result[TC[-2]]
        if("T" in TC[-1]):
            TC[-1] = result[TC[-1]]
        result["T"+str(val)] = float(TC[-2]) * float(TC[-1])
        TC.pop()
        TC.pop()
        TC.append("T"+str(val))
        val += 1
    if(I == 5):
        tac["T"+str(val)] = TC[-2] + " / " + TC[-1]
        if("T" in TC[-2]):
            TC[-2] = result[TC[-2]]
        if("T" in TC[-1]):
            TC[-1] = result[TC[-1]]
        result["T"+str(val)] = float(TC[-2]) / float(TC[-1])
        TC.pop()
        TC.pop()
        TC.append("T"+str(val)) 
        val += 1
    return TC
        
def LR_1(E, PT, Productions):
    global Nd
    S, TC, top, i = ["S0"], list(), "S0", 0
    show = int(input("To show the stack type 1: "))
    if(show == 1):
        print(S, E[i:])
    if("num" in E[i]):
        S.append(E[i])
        i += 1
        S.append(PT["num"][top])
        top = S[-1]
    else:
        S.append(E[i])
        i += 1
        S.append(PT["("][top])
        top = S[-1]
    while(1):
        e = E[i]
        if("num" in e):
            e = "num"
        G = PT[e][top]
        if(show == 1):
            print(S, E[i:])
        if(G == ""):
            print("Expression is invalid")
            return False
        elif(G == "Accept"):
            print("Expression is Valid")
            break
        elif("S" in G and i < len(E)-1):
            S.append(E[i])
            i += 1
            S.append(G)
            top = G
        else:
            I, n = Productions.index(G), int()
            if(I == 8):
                n = Nd[S[-2]]
                TC.append(n)
            else:
                TC = TAC(TC, I)
            G = G.replace("->", " ")
            G = G.split()
            if(G[1] == "num"):
                l = 1
            else:
                l = len(G[1])
            S = S[0:len(S)-2*l] 
            top = S[-1]
            S.append(G[0])
            S.append(PT[G[0]][top])
            top = S[-1]
    return True

if __name__ == "__main__":
    Expr = input("Enter any Expression: ")
    validExpr, k = re.sub('[-0-9+*()/]', "", Expr), 0
    if(len(validExpr) != 0):
        k = 1 
        print("Expression contains invalid symbols")
    Expr = Expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    Expr = Expr.replace('(', ' ( ').replace(')', ' ) ')
    Expr, i = Expr.split(), 1
    for e in range(len(Expr)):
        if(Expr[e].isdigit()):
            Nd["num"+str(i)] = Expr[e]
            Expr[e] = "num"+str(i)
            i += 1
    Parse_Table = pd.read_csv('Parse_Table.csv', header = 0).fillna('')
    del Parse_Table["Unnamed: 0"]
    index = ["S" + str(p) for p in Parse_Table.index]
    Parse_Table.index = index
    f_nt, f_t = open("NT.txt", "r"), open("T.txt", "r")
    NT, T = f_nt.readlines(), f_t.readlines() 
    f_nt.close()
    f_t.close()
    NT, T = [n[:len(n)-1] for n in NT], [t[:len(t)].split() for t in T]
    Productions = []
    for i in range(0, len(NT)):
        Productions.append(NT[i]+"->"+"".join(T[i]))
    if(k == 0):
        V = LR_1(Expr+["$"], Parse_Table, Productions)
    if(V):
        print("Three-Address code for the given expression: ")
        for t in tac:
            print(t + " = " + tac[t])
        print("Value of the Expression: " +  str(result["T" + str(val-1)]))