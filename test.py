import sys
specialChars= set()
noSpecialChar={".","\r","\n"}
activationChars= {'=', '&', '*', '-', '#', '$', '+', '%', '/', '@'}

""" for line in sys.stdin:            
    for lineChar in line:
        if lineChar in noSpecialChar:pass
        elif lineChar.isdigit():pass
        else: specialChars.add(lineChar)

print(specialChars) """


def checkSpecialCharsAroundNumber(matrix, x, y):
    specialCharAround = ""
    #top left corner
    if x==0 and y==0:
        # >
        if matrix[x+1][y] in activationChars:specialCharAround += "Right"
        # v
        if matrix[x][y+1] in activationChars:specialCharAround += "Down"
         # v->
        if matrix[x+1][y+1] in activationChars:specialCharAround += "Downright"
    #top mid line
    elif x > 0 and x < len(matrix[x])-1 and y==0:
        # >
        if matrix[x+1][y] in activationChars:specialCharAround += "Right"
        # v->
        if matrix[x+1][y+1] in activationChars:specialCharAround += "Downright"
        # v
        if matrix[x][y+1] in activationChars:specialCharAround += "Down"
        # <-v
        if matrix[x-1][y+1] in activationChars:specialCharAround += "Downleft"
        # <
        if matrix[x-1][y] in activationChars:specialCharAround += "Left"
    #top right corner
    elif x > 0 and x == len(matrix[x])-1 and y==0:
        # v
        if matrix[x][y+1] in activationChars:specialCharAround += "Down"
        # <-v
        if matrix[x-1][y+1] in activationChars:specialCharAround += "Downleft"
        # <
        if matrix[x-1][y] in activationChars:specialCharAround += "Left"
    return specialCharAround

y=0

ar = [
    ['2','#','3','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
]

for x in range(len(ar[y])):
    specChar=checkSpecialCharsAroundNumber(ar,x,y)
    counter=0
    print("[" + str(x) + "," + str(y) + "] - " +  specChar)
    print(ar[x][y])
    if len(specChar)>0 and ar[x][y].isdigit():
        counter+=int(ar[x][y])
        print("counter = " + str(counter))
        ar[x][y]=0
print("prehozene X a Y v pruchodu")


    
