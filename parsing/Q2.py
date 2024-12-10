def match(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if(a[i] != b[i]):
            return count
        count += 1
    return count

def SubSequence(a):
    S, key = a[0], 0
    if(a == ['']):
        return ''
    for i in range(1, len(a)):
        k = match(S, a[i])
        if(k != 0):
            S = a[i][:k]
            key = 1
        elif(S == a[0] and key == 0):
            S = a[i]
    if((S == a[0] or S == a[i]) and key == 0):
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
                T[i][j] = '\u03B5'
    print("\n")
    for c in range(len(T)):
        T[c].sort()
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
    LeftFactoring(NT, T)
        