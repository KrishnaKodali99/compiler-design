import re

def Tokens(l):
    relop = ['<', '>', '=']
    tokens = ['if', 'else', 'then']
    alphanum = [chr(ord('a')+i) for i in range(26)] + [chr(ord('A')+i) for i in range(26)] + [chr(ord('0')+i) for i in range(10)]
    for c in l:
        if(c in tokens):
            print('(' + c + ', ' + c + ')')
        else:
            Id = re.sub('[^a-zA-Z0-9]', ' ', c)
            op = re.sub('[a-zA-Z0-9]', ' ', c)
            unid = re.sub('[a-zA-Z0-9<>=]', ' ', c)
            Id, op, unid = Id.split(), op.split(), unid.split()
            a, b, u, i = 0, 0, 0, 0
            while(i < len(c)):
                if(c[i] in relop and a < len(op)):
                    print('(relop, ' + op[a] + ')')
                    i += len(op[a])
                    a += 1
                    continue
                elif(c[i] in alphanum and b < len(Id)):
                    if(len(re.sub('[^0-9]', '', Id[b])) == len(Id[b])):
                        print('(number, ' + Id[b] + ')')
                    else:
                        print('(id, ' + Id[b] + ')')
                    i += len(Id[b])
                    b += 1
                    continue
                elif(u < len(unid)):
                    print('(unidentified, ' + unid[u] + ')')
                    i += len(unid[u])
                    u += 1
                    continue
                break
    pass

if __name__ == "__main__":
    s = input()
    l = s.split()
    Tokens(l)
  
    