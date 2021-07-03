NT, T = [], []

def first(First, index):
    i = 0
    while(i != len(First[index])):
        f = First[index][i]
        if(f in NT):
            k = NT.index(f)
            for j in range(len(First[k])):
                if(First[k][j] not in First[index]):
                    First[index].append(First[k][j])
        i += 1
    return First

def firstSymbols(First, index):
    global NT
    global T
    for i in range(len(T[index])):
        t = T[index][i][0]
        if(t not in First[index]):
            First[index].append(t)
    return First

if __name__ == "__main__":
    s = []
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
    First = ['']*len(NT)
    for i in range(len(NT)):
        First[i] = ['']
    for i in range(len(NT)):
        First = firstSymbols(First, i)
        First[i].pop(0)
        First[i].sort()
    for i in range(len(NT)):
        First = first(First, i)
    for i in range(0, len(First)):
        First[i].sort(reverse = True)
        while(First[i][-1].isupper()):
            First[i].pop()
        First[i].sort()
    for i in range(len(NT)):
        print("First(%s)" % NT[i] + " = " + ','.join(First[i]))
        