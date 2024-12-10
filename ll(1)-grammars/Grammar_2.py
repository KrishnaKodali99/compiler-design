NT, T = [], []
Parse_Table, Stack = [], ["$", "P"]

def row(s):
    if(s == "P"):
        return 0
    elif(s == "DL"):
        return 1
    elif(s == "D"):
        return 2
    elif(s == "TY"):
        return 3
    elif(s == "VL"):
        return 4
    elif(s == "VL'"):
        return 5
    elif(s == "SL"):
        return 6
    elif(s == "S"):
        return 7
    elif(s == "ES"):
        return 8
    elif(s == "IS"):
        return 9
    elif(s == "IS'"):
        return 10
    elif(s == "WS"):
        return 11
    elif(s == "IOS"):
        return 12
    elif(s == "PE"):
        return 13
    elif(s == "BE"):
        return 14
    elif(s == "BE'"):
        return 15
    elif(s == "AE"):
        return 16
    elif(s == "AE'"):
        return 17
    elif(s == "NE"):
        return 18
    elif(s == "RE"):
        return 19
    elif(s == "RE'"):
        return 20
    elif(s == "E"):
        return 21
    elif(s == "E'"):
        return 22
    elif(s == "T"):
        return 23
    elif(s == "T'"):
        return 24
    elif(s == "F"):
        return 25
    
def col(s):
    if(s == "prog"):
        return 0
    elif(s == "int"):
        return 1
    elif(s == "float"):
        return 2
    elif(s == "if"):
        return 3
    elif(s == "else"):
        return 4
    elif(s == "then"):
        return 5
    elif(s == "and"):
        return 6
    elif(s == "or"):
        return 7
    elif(s == "not"):
        return 8
    elif(s == "do"):
        return 9
    elif(s == "while"):
        return 10
    elif(s == "end"):
        return 11
    elif(s == "print"):
        return 12
    elif(s == "scan"):
        return 13
    elif(s == "str"):
        return 14
    elif(s == "id"):
        return 15
    elif(s == "ic"):
        return 16
    elif(s == "fc"):
        return 17
    elif(s == "+"):
        return 18
    elif(s == "-"):
        return 19
    elif(s == "*"):
        return 20
    elif(s == "/"):
        return 21
    elif(s == "="):
        return 22
    elif(s == "<"):
        return 23
    elif(s == ">"):
        return 24
    elif(s == "("):
        return 25
    elif(s == ")"):
        return 26
    elif(s == "{"):
        return 27
    elif(s == "}"):
        return 28
    elif(s == ":="):
        return 29
    elif(s == ";"):
        return 30

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
    NT = ["P", "DL", "D", "TY", "VL", "VL'", "SL", "S", "ES", "IS", "IS'", "WS", "IOS", "PE", "BE", "BE'", "AE", 
          "AE'", "NE", "RE", "RE'", "E", "E'", "T", "T'", "F"]
    Parse_Table = [['' for j in range(31)] for i in range(26)]
    Parse_Table[0][0] = ["prog", "DL", "SL", "end"]
    Parse_Table[1][1], Parse_Table[1][2] = ["D", "DL"], ["D", "DL"]
    Parse_Table[2][1], Parse_Table[2][2] = ["TY", "VL", ";"], ["TY", "VL", ";"]
    Parse_Table[3][1], Parse_Table[3][2] = ["int"], ["float"]
    Parse_Table[4][15] = ["id", "VL'"]
    Parse_Table[5][15] = ["VL"]
    Parse_Table[6][15], Parse_Table[6][3], Parse_Table[6][10] = ["S", "SL"], ["S", "SL"], ["S", "SL"]
    Parse_Table[6][12], Parse_Table[6][13] = ["S", "SL"], ["S", "SL"]
    Parse_Table[7][15], Parse_Table[7][3], Parse_Table[7][10] = ["ES"], ["IS"], ["WS"]
    Parse_Table[7][12], Parse_Table[7][13] = ["IOS"], ["IOS"]
    Parse_Table[8][15] = ["id", ":=", "E", ";"]
    Parse_Table[9][3] = ["if","BE", "then", "SL", "IS'"]
    Parse_Table[10][11], Parse_Table[10][4] = ["end"], ["else", "SL", "end"]
    Parse_Table[11][10] = ["while", "BE", "do", "SL", "end"]
    Parse_Table[12][12], Parse_Table[12][13] = ["print", "PE"], ["scan", "id"]
    Parse_Table[13][25], Parse_Table[13][15], Parse_Table[13][16] = ["E"], ["E"], ["E"]
    Parse_Table[13][17], Parse_Table[13][14] = ["E"], ["str"]
    Parse_Table[14][8], Parse_Table[14][27], Parse_Table[14][25] = ["AE", "BE'"], ["AE", "BE'"], ["AE", "BE'"]
    Parse_Table[14][15], Parse_Table[14][16], Parse_Table[14][17] = ["AE", "BE'"], ["AE", "BE'"], ["AE", "BE'"]
    Parse_Table[15][7] = ["or", "AE", "BE'"]
    Parse_Table[16][8], Parse_Table[16][27], Parse_Table[16][25] = ["NE", "AE'"], ["NE", "AE'"], ["NE", "AE'"]
    Parse_Table[16][15], Parse_Table[16][16], Parse_Table[16][17] = ["NE", "AE'"], ["NE", "AE'"], ["NE", "AE'"]
    Parse_Table[17][6] = ["and", "NE", "AE'"]
    Parse_Table[18][8], Parse_Table[18][27], Parse_Table[18][25] = ["not", "NE'"], ["{", "BE", "}"], ["RE"]
    Parse_Table[18][15], Parse_Table[18][16], Parse_Table[18][17] = ["RE"], ["RE"], ["RE"]
    Parse_Table[19][25], Parse_Table[19][15], Parse_Table[19][16] = ["E", "RE'"], ["E", "RE'"], ["E", "RE'"]
    Parse_Table[19][17] = ["E", "RE'"]
    Parse_Table[20][22], Parse_Table[20][23], Parse_Table[20][24] = ["=", "E"], ["<", "E"], [">", "E"]
    Parse_Table[21][25], Parse_Table[21][15], Parse_Table[21][16] = ["T", "E'"], ["T", "E'"], ["T", "E'"]
    Parse_Table[21][17] = ["T", "E'"] 
    Parse_Table[22][18], Parse_Table[22][19] = ["+", "T", "E'"], ["-", "T", "E'"]
    Parse_Table[23][25], Parse_Table[23][15], Parse_Table[23][16] = ["F", "T'"], ["F", "T'"], ["F", "T'"]
    Parse_Table[23][17] = ["F", "T'"]
    Parse_Table[25][25], Parse_Table[25][15], Parse_Table[25][16] = ["(", "E", ")"], ["id"], ["ic"]
    Parse_Table[25][17] = ["fc"]
    Parse_Table[24][20], Parse_Table[24][21] = ["*", "F", "T'"], ["/", "F", "T'"]
    Parse_Table[6][11], Parse_Table[6][4] = ["\u03B5"], ["\u03B5"]
    Parse_Table[1][15], Parse_Table[1][3], Parse_Table[1][10] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[1][11], Parse_Table[1][12], Parse_Table[1][13] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[1][4] = ["\u03B5"]
    Parse_Table[5][30] = ["\u03B5"]
    Parse_Table[15][9], Parse_Table[15][5], Parse_Table[15][28] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[17][7], Parse_Table[17][9], Parse_Table[17][5] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[17][28] = ["\u03B5"]
    Parse_Table[22][22], Parse_Table[22][23], Parse_Table[22][24] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[22][6], Parse_Table[22][7], Parse_Table[22][9] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[22][5], Parse_Table[22][28], Parse_Table[22][15] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[22][3], Parse_Table[22][10], Parse_Table[22][12] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[22][13], Parse_Table[22][11], Parse_Table[22][4] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[22][30] = ["\u03B5"]
    Parse_Table[24][22], Parse_Table[24][23], Parse_Table[24][24] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[24][6], Parse_Table[24][7], Parse_Table[24][9] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[24][5], Parse_Table[24][28], Parse_Table[24][15] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[24][3], Parse_Table[24][10], Parse_Table[24][12] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[24][13], Parse_Table[24][11], Parse_Table[24][4] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    Parse_Table[24][18], Parse_Table[24][19], Parse_Table[24][30] = ["\u03B5"], ["\u03B5"], ["\u03B5"]
    
    f = open("G2tokens.txt", "r")
    s = list()
    for i in f:
        s.append(i[:-1])
    f.close()
    print("To show Stack and Remaining input at each step Type 1, else 0")
    details = int(input())
    k = PredictiveParsing(s, details)
    if(k == 1):
        print("Program accepeted by Grammar")
    else:
        print("Program not accepted by Grammar")
    
    
    