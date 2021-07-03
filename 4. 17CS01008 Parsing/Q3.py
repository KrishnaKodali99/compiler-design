import re

it, error, S = 0, 0, str()

def E():
    if(it == len(S)):
        return
    T()
    E1()
    return
    
def E1():
    global it
    if(it == len(S)):
        return
    if(S[it] == '+'):
        it += 1
        T()
        E1()
    return

def T():
    if(it == len(S)):
        return
    F()
    T1()
    return 

def T1():
    global it
    if(it == len(S)):
        return
    if(S[it] == '*'):
        it += 1
        F()
        T1()
    return
        
def F():
    global it
    if(it == len(S)):
        return
    if(S[it] == 'id'):
        it += 1
    elif(S[it] == '('):
        it += 1
        E()
        if(S[it] == ')'):
            it += 1
        else:
            error = 1
    else:
        error = 1
    return 

NTE = ['E', "E'", "T", "T'", "F"]
TE  = [["TE'"], ["+TE'", "\u03B5"], ["FT'"], ["*FT'", "\u03B5"], ["(E)", "id"]]
                
if __name__ == "__main__":
    print("The Context Free Grammar is: ")
    for i in range(len(TE)):
        print(NTE[i] +  ' -> ' + ' | '.join(TE[i]))
    print('\nEnter the String')
    S = input()
    S, op = S.replace(' ', ''), ['+', '*', ')', '(']
    S = re.sub('[^+*()]', 'id', S)
    S = S.replace('+', ' + ')
    S = S.replace('*', ' * ')
    S = S.replace('(', ' ( ')
    S = S.replace(')', ' ) ')
    S = S.split()
    E()
    if(len(S) == it and error == 0):
        print("String is Accepted by Grammar")
    else:
        print("String is Rejected by Grammar")
    
 
        
        
    
    