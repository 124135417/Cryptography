import  sympy as sp
from sympy.parsing.sympy_parser import parse_expr



input = [0,1,0,1,0,1,1,0, 1,1,1,0,0,0,1,0,
         0,0,0,1,1,0,0,1, 1,0,1,1,0,0,1,0,
         0,1,0,0,0,1,0,0, 1,0,1,1,0,0,1,1,
         1,1,0,1,1,0,1,1, 0,1,0,0,0,0,1,1,
         1,0,0,0,0,0,0,1, 0,0,0,1,1,1,1,0,
         1,0,0,1,1,1,0,1, 0,0,1,1,1,0,1,0,
         1,0,0,1,1,1,1,0, 1,0,0,0,0,1,0,1,
         1,1,1,1,0,0,1,1, 0,1,0,0,1,1,1,1]

mixTable = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

sbox = "63,7c,77,7b,f2,6b,6f,c5,30,01,67,2b,fe,d7,ab,76,ca,82,c9,7d,fa,59,47,f0,ad,d4,a2,af,9c,a4,72,c0,b7,fd,93,26,36,3f,f7,cc,34,a5,e5,f1,71,d8,31,15,04,c7,23,c3,18,96,05,9a,07,12,80,e2,eb,27,b2,75,09,83,2c,1a,1b,6e,5a,a0,52,3b,d6,b3,29,e3,2f,84,53,d1,00,ed,20,fc,b1,5b,6a,cb,be,39,4a,4c,58,cf,d0,ef,aa,fb,43,4d,33,85,45,f9,02,7f,50,3c,9f,a8,51,a3,40,8f,92,9d,38,f5,bc,b6,da,21,10,ff,f3,d2,cd,0c,13,ec,5f,97,44,17,c4,a7,7e,3d,64,5d,19,73,60,81,4f,dc,22,2a,90,88,46,ee,b8,14,de,5e,0b,db,e0,32,3a,0a,49,06,24,5c,c2,d3,ac,62,91,95,e4,79,e7,c8,37,6d,8d,d5,4e,a9,6c,56,f4,ea,65,7a,ae,08,ba,78,25,2e,1c,a6,b4,c6,e8,dd,74,1f,4b,bd,8b,8a,70,3e,b5,66,48,03,f6,0e,61,35,57,b9,86,c1,1d,9e,e1,f8,98,11,69,d9,8e,94,9b,1e,87,e9,ce,55,28,df,8c,a1,89,0d,bf,e6,42,68,41,99,2d,0f,b0,54,bb,16".split(",")

roundKey = [0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0]
#convert binary into hex
hexa = []
for i in range(0, len(input), 8): 
    x = i 
    hexa.append(input[x:x+8]) 
    
for i in range(len(hexa)):
    hexa[i] = str(hex(int("".join(str(x) for x in hexa[i]), 2)))[2:]
# print(hexa)

#convert hex into 4x4 matrix
state=[]
temp=[]
num=0
for i in range(4):
    for x in range(4):
        temp.append(hexa[num])
        num=num+1
    state.append(temp)
    temp=[]
# print(state)

#convert sbox into 16x16 matrix
sboxConverted=[]
for i in range(0, len(sbox), 16): 
    x = i 
    sboxConverted.append(sbox[x:x+16]) 
# print(sboxConverted)

#pick value from input to sbox
for i in range(4):
    for x in range(4):
        state[i][x] = sboxConverted[int(state[i][x][0],16)][int(state[i][x][1],16)]
# print(state)

#rotate second row one to the left, third two to the left and fourth row three to the left
for i in range(1,4):
    state[i] = state[i][i:]+state[i][:i]
# print(state)

#convert mix table into egiht digits binary form
for i in range(4):
    for x in range(4):
        mixTable[i][x] = str(bin(mixTable[i][x]))[2:]
        if len(mixTable[i][x]) == 1:
            mixTable[i][x] = "000"+mixTable[i][x]
        elif len(mixTable[i][x]) == 2:
            mixTable[i][x] = "00"+mixTable[i][x]
        elif len(mixTable[i][x]) == 3:
            mixTable[i][x] = "0"+mixTable[i][x]

#append four zero to each binary on left side
for i in range(4):
    for x in range(4):
        mixTable[i][x] = "0000"+mixTable[i][x]
    # print(mix[i])

#function for expand the polynomial
def expand_polynomial(expr):
    expanded_expr = sp.expand(expr)
    return expanded_expr

#convert hexa to binary
for i in range(4):
    for x in range(4):
        state[i][x] = str(bin(int(state[i][x],16)))[2:]
        if len(state[i][x]) == 6:
            state[i][x] = "00"+state[i][x]
        elif len(state[i][x]) == 5:
            state[i][x] = "000"+state[i][x]
        elif len(state[i][x]) == 4:
            state[i][x] = "0000"+state[i][x]
        elif len(state[i][x]) == 7:
            state[i][x] = "0"+state[i][x]
        
# print(mixTable)
# print(state)

#convert mix table into polynomial
for i in range(4):
    for x in range(4):
        if mixTable[i][x][-2:] == "10":
            mixTable[i][x] = "x"
        elif mixTable[i][x][-2:] == "01":
            mixTable[i][x] = "1"
        elif mixTable[i][x][-2:] == "11":
            mixTable[i][x] = "x+1"

# print(mixTable)
# print(state)

#convert state into polynomial
for i in range(4):
    for x in range(4):
        for y in range(8):
            if state[i][x][8-1-y] == "1":
                #remove zeros before x

                state[i][x] = state[i][x][:8-1-y]+"x**"+str(y)+"+"+state[i][x][8-1-y+1:]
        state[i][x] = state[i][x][:-1]
        if state[i][x][-1] == "+":
            state[i][x] = state[i][x][:-1]

#remove all the "0000" before x
for i in range(4):
    for x in range(4):
        if state[i][x][:4] == "0000":
            state[i][x] = state[i][x][4:]
        elif state[i][x][:3] == "000":
            state[i][x] = state[i][x][3:]
        elif state[i][x][:2] == "00":
            state[i][x] = state[i][x][2:]
        elif state[i][x][:1] == "0":
            state[i][x] = state[i][x][1:]
        if state[i][x][-1] == "+":
            state[i][x] = state[i][x][:-1]

#remove all 000
for i in range(4):
    for x in range(4):
        state[i][x]=state[i][x].replace("000","")
        state[i][x]=state[i][x].replace("00","")
        state[i][x]=state[i][x].replace("0x","x")
        state[i][x]=state[i][x].replace("+0","")
        state[i][x]=state[i][x].replace("x**0","1")
        state[i][x]=state[i][x].replace("x**1","x")

# print(state)
#convert polynomial into binary
# def convertPolytoBinary(list):
#     for i in list

#matrix multiplication
result = []
# for i in range(4):
#     for x in range(4):
#         for y in range(4):
#             result[i,x] = expand_polynomial(parse_expr(state[i][y])*parse_expr(mixTable[y][x]))


# Import matrix after mix column
mixed=[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0]
print(mixed)
#xor between mixed and roundKey
for i in range(len(mixed)):
    mixed[i] = mixed[i] ^ roundKey[i]

print(roundKey)
print(mixed)

expanded_expression = expand_polynomial(parse_expr(state[0][0])*parse_expr(mixTable[0][0]))

        
# 示例
x = sp.symbols('x')
expression = x*(x**7 + x**2 + x)
# expanded_expression = expand_polynomial(expression)
# print(expanded_expression)
