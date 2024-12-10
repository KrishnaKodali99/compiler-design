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
            T[i] = NL; NP.append('\u03B5')
            NT.insert(i+1, NT[i] + "'"*t)
            T.insert(i+1, NP)
        i += 1
        
    print("\n")
    for c in range(len(T)):
        if(T[c] != ['']):
            print(NT[c] + ' -> ' + ' | '.join(T[c]))
            
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
    LeftRecursion(NT, T)