def match(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if(a[i] != b[i]):
            return count
        count += 1
    return count

def SubSequence(a):
    S = a[0]
    if(a == ['']):
        return ''
    for i in range(1, len(a)):
        k = match(S, a[i])
        if(k != 0):
            S = a[i][:k]
        elif(S == a[0]):
            S = a[i]
    if(S == a[0] or S == a[i]):
        return ''
    return S
        
def LeftFactoring(NT, T):
    i, ln = 0, len(NT)
    while(i != len(NT)):
        L = str()
        T[i].sort()
        L = SubSequence(T[i])
        p = []
        for j in range(len(T[i])):
            if(T[i][j][:len(L)] == L) :
                p.append(T[i][j][len(L):])
                t = 1
                while(1):
                    if(NT[i] + "'"*t in NT):
                        t += 1
                    else:
                        break
                T[i][j] = L + NT[i] + "'"*t
        T[i] = list(set(T[i]))
        if(len(L) > 0):
            t = 1
            while(1):
                    if(NT[i] + "'"*t in NT):
                        t += 1
                    else:
                        break
            NT.insert(i+1, NT[i] + "'"*t)
            T.insert(i+1, p)
        elif(len(L) == 0):
            T[i] = list(p)
        i += 1
    for i in range(len(T)):
        for j in range(len(T[i])):
            if(T[i][j] == ''):
                T[i][j] = '#'
    return(NT, T)
        
def LeftRecursion(NT, T):
    i = 0
    while(i != len(NT)):
        NL, NP, k = [], [], 0
        for j in range(len(T[i])):
            if(T[i][j][:len(NT[i])] == NT[i]):
                k = 1
                break
        if(k == 1):
            t = 1
            while(1):
                    if(NT[i] + "'"*t in NT):
                        t += 1
                    else:
                        break
            for j in range(len(T[i])):
                if(T[i][j][:len(NT[i])] != NT[i]):
                    NL.append(T[i][j])
            for j in range(len(T[i])):
                if(T[i][j][:len(NT[i])] == NT[i]):
                    NP.append(T[i][j][len(NT[i]):])
            for j in range(len(NL)):
                NL[j] = NL[j] + NT[i] + "'"*t
            for j in range(len(NP)):
                NP[j] = NP[j] + NT[i] + "'"*t
            T[i] = NL; NP.append('#')
            NT.insert(i+1, NT[i] + "'"*t)
            T.insert(i+1, NP)
        i += 1
    return(NT, T)
            
if __name__ == "__main__":
    s, NT, T = [], [], []
    print("To stop giving CFG as input type Exit")
    while(1):
        inp = input()
        if(inp == 'Exit'):
            break
        if(inp != '\n'):
            s.append(inp)  
    for l in s:
        l = l.replace(' ', '')
        nt, i = str(), 0
        for c in l:
            i += 1
            if(c == '-'):
                break
            if(c != '\n'):
                nt += c
        NT.append(nt)
        l = l[i+1:]
        l = l.replace('|', ' ')
        l = l.split()
        T.append(l)
    NT, T = LeftFactoring(NT, T)
    NT, T = LeftRecursion(NT, T)

    for i in range(len(T)):
        for j in range(len(T[i])):
            if(T[i][j] == ''):
                T[i][j] = '#'
    print("\n")
    f = open("grammarLL.txt", 'w')
    for nt in NT:
        f.write("%s " % nt)
    f.write("\n")
    for t in T:
        for ter in t:
            f.write("%s " % ter)
        f.write("\n")
    f.close()
    for c in range(len(T)):
        print(NT[c] + ' -> ' + ' | '.join(T[c]))
    print("\n# represents epsilon")