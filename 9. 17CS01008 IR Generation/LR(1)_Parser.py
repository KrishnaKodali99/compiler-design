import pandas as pd

NT, T, NT_set, T_set, Actions, first = list(), list(), set(), set(), list(), dict()
States, Goto, Goto_States = list(), list(),list()

class Items:
    global NT, T, NT_set, first
    def __init__(self, index, F, dindex):
        self.lp, self.rp = NT[index], list()
        self.index= index
        for i in range(len(T[index])):
            self.rp.append(T[index][i])
        self.rp.insert(dindex, '.')
        self.dindex, self.f = dindex, F
    
    def __eq__(self, other):
        if not isinstance(other, Items):
            return NotImplemented
        return (self.dindex == other.dindex and self.f == other.f and self.index == other.index)
        
def Closure(nt):
    I = []
    for i in range(len(NT)):
        if(NT[i] == nt):
            I.append(i)
    return I

def Verify(I, L):
    for i in range(len(L)):
        if(I == L[i]):
            return False
    return True

def SearchState(L):
    for i in range(len(States)):
        S, k = States[i], 0
        if(len(L) == len(S)):
            for j in range(len(S)):
                if(L[j] == S[j]):
                    k += 1
        if(k == len(L)):
            return i
    return -1

def StartState():
    global NT, T, NT_set, first, States
    I, L, G, i = Items(0, '$', 0), list(), [], 0
    L.append(I)
    while(i < len(L)):
        I = L[i]
        di, rp = I.dindex, I.rp
        rp.append('#')
        if(rp[di+1] in NT_set):
            f = '$'
            if(di+2 < len(rp) and rp[di+2] != '#'):
                if(rp[di+2] in NT_set):
                    f = first[rp[di+2]]
                else:
                    f = rp[di+2]
            elif(di+2 < len(rp) and rp[di+2] == '#'):
                f = I.f
            indices = Closure(rp[di+1])
            for ind in indices:
                It = Items(ind, f, 0)
                if(Verify(It, L)):
                    L.append(It)
        rp.pop()
        i += 1
    for i in range(len(L)):
        I = L[i]
        di = I.dindex
        if(di != len(I.rp)-1):
            G.append(I.rp[di+1])
    States.append(L)
    Goto.append(G)
        
def LR_1():
    global NT, T, NT_set, first, States, Goto, Goto_States
    i = 0
    while(i < len(States)):
        S, G = States[i], Goto[i]
        GS = list()
        for p in range(len(G)):
            g, L, GG = G[p], list(), list()
            for j in range(len(S)):
                I = S[j]
                di, rp = I.dindex, I.rp
                if(di == len(I.rp)-1):
                    continue
                if(rp[di+1] == g):
                    new_I = Items(I.index, I.f, di+1)
                    L.append(new_I)
            if(len(L) > 0):
                k = 0
                while(k < len(L)):
                    I = L[k]
                    di, rp = I.dindex, I.rp
                    rp.append('#')
                    if(rp[di+1] in NT_set):
                        f = I.f
                        if(di+2 < len(rp) and rp[di+2] != '#'):
                            if(rp[di+2] in NT_set):
                                f = first[rp[di+2]]
                            else:
                                f = rp[di+2]
                        elif(di+2 < len(rp) and rp[di+2] == '#'):
                            f = I.f
                        indices = Closure(rp[di+1])
                        for ind in indices:
                             It = Items(ind, f, 0)
                             if(Verify(It, L)):
                                 L.append(It)
                    rp.pop()
                    k += 1
            for p in range(len(L)):
                I = L[p]
                di = I.dindex
                if(di != len(I.rp)-1):
                    GG.append(I.rp[di+1])
            SS = SearchState(L)
            if(SS == -1 and len(L) != 0):
                States.append(L)
                Goto.append(GG)
                GS.append(len(States)-1)
            else:
                GS.append(SS)
        Goto_States.append(GS)
        i += 1
    
def LR1_Automaton():
    print("The transitions in DFA are: ")
    l, Tr = len(Goto), list()
    for i in range(l):
        G, GS = Goto[i], Goto_States[i]
        for j in range(len(G)):
            if(G != []):
                P = "S" + str(i) + " -> " + "S" + str(GS[j]) +" , " + G[j]
                if(P not in Tr):
                    Tr.append(P)
    for i in Tr:
        print(i) 
        
def LR1_ParseTable():
    global NT, T, NT_set, first, States, Goto, Goto_States
    r, c = len(States), len(NT_set) + len(T_set) + 1 
    ParseTable = [['' for j in range(c)] for i in range(r)]
    NT_list, T_list = list(NT_set), list(T_set)
    NT_list.sort(), T_list.sort()
    for i in range(len(States)):
        S, G, GS = States[i], Goto[i], Goto_States[i]
        r = i
        for j in range(len(S)):
            I = S[j]
            di = I.dindex
            rp = I.rp
            if(di == len(rp)-1):
                index, F = I.index, I.f
                if(F == "$"):
                    c = 0
                    if(index == 0):
                        ParseTable[r][c] = "Accept"
                    else:
                        if(ParseTable[r][c] == ""):
                            ParseTable[r][c] = NT[index] + '->' + ''.join(T[index])
                        elif((NT[index] + '->' + ''.join(T[index])) not in ParseTable[r][c]):
                            ParseTable[r][c] += ", " +  NT[index] + '->' + ''.join(T[index])
                else:
                    for k in range(len(F)):
                        c = T_list.index(F[k]) + 1
                        if(ParseTable[r][c] == ""):
                            ParseTable[r][c] = NT[index] + '->' + ''.join(T[index])
                        elif((NT[index] + '->' + ''.join(T[index])) not in ParseTable[r][c]):
                            ParseTable[r][c] += ", " + NT[index] + '->' + ''.join(T[index])
            else:
                index = G.index(rp[di+1])
                if(rp[di+1] in NT_set):
                    c = NT_list.index(rp[di+1]) + len(T_list) + 1
                elif(rp[di+1] in T_set):
                    c = T_list.index(rp[di+1]) + 1
                else:
                    c = 0
                if(ParseTable[r][c] == ""):
                    ParseTable[r][c] = 'S' + str(GS[index])            
                elif(('S' + str(GS[index])) not in ParseTable[r][c]):
                    ParseTable[r][c] += "," + 'S' + str(GS[index])
    Symbols = ["$"] + T_list + NT_list
    df = pd.DataFrame(ParseTable, columns = Symbols)
    return df
    
def First(index):
    global NT, T, NT_set, first
    nt, t = NT[index], T[index]
    if(nt not in first):
        first[nt] = list()
    if(t[0] not in first[nt]):
        first[nt].append(t[0])

def FirstPenUltimate(index):
    global NT, T, NT_set, first
    nt, t, l = NT[index], T[index], len(T[index])
    for i in range(0, l-1):
        if(t[i] in NT_set and '#' in first[t[i]]):
            first[nt].append(t[i+1])
        elif(t[i] in NT_set and '#' not in first[t[i]]):
            break
        elif(t[i] not in NT_set):
            break
       
def FinalFirst(nt):
    global NT, T, NT_set, first
    L, i = first[nt], 0
    while(i < len(L)):
        if(L[i] == nt and '#' not in L):
            L.pop(i)
            i -= 1
        elif(L[i] in NT_set):
            F = first[L[i]]
            for j in range(len(F)):
                if(F[j] not in L):
                    L.append(F[j])
            L.pop(i)
            i -= 1
        i += 1
    return L

if __name__ == "__main__":
    St = list()
    print("Type Exit to stop giving input and use # for epsilon")
    print("Enter the productions:")
    while(1):
        inp = input()
        if(inp.lower() == 'exit'):
            break
        else:
            St.append(inp)
    for i in range(len(St)):
        s = St[i].replace('->', '')
        s = s.replace('|', ' | ').replace('{', ' { ').replace('}', ' } ')
        s = s.split()
        L = list()
        for j in range(1, len(s)):
            if(s[j] == '|'):
                NT.append(s[0])
                T.append(L)
                L = list()
            elif(s[j] ==  "{"):
                Actions.append(s[j+1:len(s)-1])
                break
            else:
                L.append(s[j])
        NT.append(s[0])
        T.append(L)
    NT_set = set(NT)
    N = list(NT_set)
    for i in range(len(NT)):
        First(i)
    for i in range(len(NT)):
        FirstPenUltimate(i)
    for i in range(len(N)):
        first[N[i]] = FinalFirst(N[i])
    for i in range(len(T)):
        for j in range(len(T[i])):
            k = T[i][j]
            if(k not in NT_set):
                 T_set.add(k)       
    StartState()
    LR_1()
    LR1_Automaton()
    df = LR1_ParseTable()
    if("S'" in df.columns):
        df = df.drop("S'", axis = 1)
    f = df.to_csv('Parse_Table.csv')
    f_nt, f_t = open("NT.txt", "w"), open("T.txt", "w")
    f_nt.writelines([n+"\n" for n in NT])
    f_nt.close()    
    f_t.writelines([" ".join(t)+"\n" for t in T])
    f_t.close()
    