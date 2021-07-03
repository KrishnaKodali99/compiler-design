import re
import pandas as pd
import networkx as nx

G = nx.DiGraph()

AS_Tree, Nd, INT, NODES = "", {}, {}, []
add, sub, mul, div = 0, 0, 0, 0
class nodeInt:
    def __init__(self, Int):
        self.Int, self.result = Int, Int

class nodeOp:
    def __init__(self, Op, L, R):
        self.Op, self.L, self.R = Op, L, R
        self.result = 0
    def __eq__(self, other):
        if not isinstance(other, nodeOp):
            return NotImplemented
        return (self.Op == other.Op and self.L == other.L and self.R == other.R)
        
def AST(AS, I, num):
    global INT, add, sub, mul, div
    if(I == 1):
        R = AS[-1]
        AS.pop()
        L = AS[-1]
        AS.pop()
        n = nodeOp("+"+str(add), L, R)
        add += 1
        AS.append(n)
    elif(I == 2):
        R = AS[-1]
        AS.pop()
        L = AS[-1]
        AS.pop()
        n = nodeOp("-"+str(sub), L, R)
        sub += 1
        AS.append(n)
    elif(I == 4):
        R = AS[-1]
        AS.pop()
        L = AS[-1]
        AS.pop()
        n = nodeOp("*"+str(mul), L, R)
        mul += 1
        AS.append(n)
    elif(I == 5):
        R = AS[-1]
        AS.pop()
        L = AS[-1]
        AS.pop()
        n = nodeOp("/"+str(div), L, R)
        div += 1
        AS.append(n)
    elif(I == 8):
        if(num in INT):
            n = INT[num]
        else:
            INT[num] = nodeInt(num)
            n = nodeInt(num)
        AS.append(n)
    return AS
        
def LR_1(E, PT, Productions):
    global Nd
    S, AS, top, i = ["S0"], list(), "S0", 0
    show = int(input("To show the stack, type 1: "))
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
            return None
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
            AS = AST(AS, I, n)
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
    return AS[0]

def Result(AS_Tree):
    if(type(AS_Tree) == nodeInt):
        return
    Result(AS_Tree.L)
    Result(AS_Tree.R)
    opr = AS_Tree.Op
    if('+' in opr):
        AS_Tree.result = float(AS_Tree.L.result) + float(AS_Tree.R.result)
    elif('-' in opr):
        AS_Tree.result = float(AS_Tree.L.result) - float(AS_Tree.R.result)
    elif('*' in opr):
        AS_Tree.result = float(AS_Tree.L.result) * float(AS_Tree.R.result)
    elif('/' in opr):
        AS_Tree.result = float(AS_Tree.L.result) / float(AS_Tree.R.result)

def Display(AS_Tree):
    global G
    if(type(AS_Tree) == nodeInt):
        return
    L, R = AS_Tree.L, AS_Tree.R
    if(type(L) == nodeOp):
        G.add_edge(AS_Tree.Op, L.Op)
    else:
        G.add_edge(AS_Tree.Op, L.Int)
    if(type(R) == nodeOp):
        G.add_edge(AS_Tree.Op, R.Op)
    else:
        G.add_edge(AS_Tree.Op, R.Int)
    Display(AS_Tree.L)
    Display(AS_Tree.R)

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
        AS_Tree = LR_1(Expr+["$"], Parse_Table, Productions)
        if(AS_Tree != None):
            Display(AS_Tree)
            nx.draw_circular(G, with_labels = True)
            Result(AS_Tree)
            print("Value of the Expression: " +  str(AS_Tree.result))
            
    
    