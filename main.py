import sys
import re

matrix = []

activationChars= {'=', '&', '*', '-', '#', '$', '+', '%', '/', '@'}


def vypis_2D_pole(pole):
    
    for radek in pole:
        output = ""
        for znak in radek:
            output+=str(znak)
        print(output)
            
def vypisPole(pole):
    print("delka pole: " + str(len(pole)))
    for radek in pole: 
            print(str(radek))

def findSpecialChars(input):
    specialChars= set()
    noSpecialChar={".","\r","\n"}

    for y in input:            
        for x in y:
            if x in noSpecialChar:pass
            elif x.isdigit():pass
            else: specialChars.add(x)
    
    return specialChars

def checkForSpecialCharsInLine():
    specialChars= set()
    noSpecialChar={".","\r","\n"}

    for line in sys.stdin:            
        for lineChar in line:
            if lineChar in noSpecialChar:pass
            elif lineChar.isdigit():pass
            else: specialChars.add(lineChar)
    
    return specialChars

def checkForAlphabetCharsInLine():
    alphaChars= set()

    for line in sys.stdin:            
        for lineChar in line:
            if lineChar.isalpha(): alphaCharsInInput=True
    
    return alphaChars

def checkSpecialCharsAroundNumber(matrix, x, y):
    specialCharAround = ""
    #top left corner
    if x==0 and y==0:
        # >
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
         # v->
        if matrix[y+1][x+1] in activationChars:specialCharAround += "Downright"
    #top mid line
    elif x > 0 and x < len(matrix[y])-1 and y==0:
        # >
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
        # v->
        if matrix[y+1][x+1] in activationChars:specialCharAround += "Downright"
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
        # <-v
        if matrix[y+1][x-1] in activationChars:specialCharAround += "Downleft"
        # <
        if matrix[y][x-1] in activationChars:specialCharAround += "Left"
    #top right corner
    elif x > 0 and x == len(matrix[y])-1 and y==0:
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
        # <-v
        if matrix[y+1][x-1] in activationChars:specialCharAround += "Downleft"
        # <
        if matrix[y][x-1] in activationChars:specialCharAround += "Left"
    #left mid column
    elif x == 0 and y>0 and y < len(matrix)-1:
        # ^
        if matrix[y-1][x] in activationChars:specialCharAround += "Top"
        # ^->
        if matrix[y-1][x+1] in activationChars:specialCharAround += "Topright"
        # >
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
         # v->
        if matrix[y+1][x+1] in activationChars:specialCharAround += "Downright"
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
    
    #mid mid
    elif x > 0 and y>0 and y < len(matrix)-1 and x<len(matrix[y])-1:
        # ^
        if matrix[y-1][x] in activationChars:specialCharAround += "Top"
        # ^->
        if matrix[y-1][x+1] in activationChars:specialCharAround += "Topright"
        # >
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
         # v->
        if matrix[y+1][x+1] in activationChars:specialCharAround += "Downright"
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
        # <-v
        if matrix[y+1][x-1] in activationChars:specialCharAround += "Downleft"
        # <
        if matrix[y][x-1] in activationChars:specialCharAround += "Left"
         # <-^
        if matrix[y-1][x-1] in activationChars:specialCharAround += "Topleft"

    #right mid column
    elif x < len(matrix[y])-1 and y>0 and y < len(matrix)-1:
        # ^
        if matrix[y-1][x] in activationChars:specialCharAround += "Top"
        # <-^
        if matrix[y-1][x-1] in activationChars:specialCharAround += "Topleft"
        # <
        if matrix[y][x-1] in activationChars:specialCharAround += "Left"
         # <-v
        if matrix[y+1][x-1] in activationChars:specialCharAround += "Downleft"
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
    
    #down left corner
    if x==0 and y== len(matrix)-1:
        # >
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
        # ^
        if matrix[y-1][x] in activationChars:specialCharAround += "Top"
         # ^->
        if matrix[y-1][x+1] in activationChars:specialCharAround += "Topright"

    #down mid line
    elif x > 0 and x < len(matrix[y])-1 and y==len(matrix)-1:
        # >
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
        # ^->
        if matrix[y-1][x+1] in activationChars:specialCharAround += "Topright"
        # ^
        if matrix[y-1][x] in activationChars:specialCharAround += "Top"
        # <-^
        if matrix[y-1][x-1] in activationChars:specialCharAround += "Topleft"
        # <
        if matrix[y][x-1] in activationChars:specialCharAround += "Left"
    
    #down right corner
    if x==len(matrix[y])-1 and y== len(matrix)-1:
        # <
        if matrix[y][x-1] in activationChars:
            specialCharAround += "Left"
        # ^
        if matrix[y-1][x] in activationChars:
            specialCharAround += "Top"
         # <-^
        if matrix[y-1][x-1] in activationChars:
            specialCharAround += "Topleft"
    return specialCharAround

def addFirstLinesIntoMatrix(ar:list):
    inputChunk = []
    if len(ar) < 5:
        while len(ar)<5 :
            inputLine = sys.stdin.readline()
            for lineChar in inputLine:
                #TODO work with EOF one line
                if lineChar != "\r":pass
                if lineChar != "\n":
                    inputChunk.append(lineChar)
                else:  
                    ar.append(inputChunk)
                    inputChunk = []
    return ar

def shiftMatrixUp(ar:list, times):
    for t in range(len(ar)-1):
        ar[t] = ar[t+1]
    
        
       
def addNextLineIntoMatrix(ar:list, inputLine):
    inputChunk = []
    for lineChar in inputLine:
        if lineChar != "\r":pass
        if lineChar != "\n":
            inputChunk.append(lineChar)
        else:
            ar[-1] = inputChunk
            
    return ar

def countNumbersAroundSpecialCharsInLineOfMatrix(ar:list, y:int, counter:int ):
    countNumber=False
    numberToConvert=""
    for x in range(len(ar[y])):
        #if str(ar[y][x])!="." :print("coor: [" + str(x) + "," + str(y) + "] = "+ str(ar[y][x]))
        if str(ar[y][x]).isdigit():
            specChar=checkSpecialCharsAroundNumber(ar,x,y)
            if len(specChar)>0: countNumber=True
            numberToConvert+=str(ar[y][x])
            if x+1<len(ar[y]) and str(ar[y][x+1]).isdigit():
                pass
            elif x==len(ar[y]) and y ==len(ar):
                counter+=int(numberToConvert)
                numberToConvert=""
                specChar=""
                countNumber=False
                #print("counter = " + str(counter))
                #vypis_pole(ar)
            else:
                if countNumber:
                    #pokud zapocitame cislo tak ho v pruchozi matici vynulujeme aby nevznikaly duplicity v souctu
                    for z in range(len(numberToConvert)):
                        ar[y][x-z]=0

                    counter+=int(numberToConvert)
                    numberToConvert=""
                    specChar=""
                    countNumber=False
                    print("counter = " + str(counter))
                    #vypis_pole(ar)
                else:
                    numberToConvert=""
                    specChar=""
                    #print("number wasnt around special char")
    return counter
    

def refactor():
    counter=0
    matrix = []
    if len(matrix)<5:
        matrix = addFirstLinesIntoMatrix(matrix)
        counter = countNumbersAroundSpecialCharsInLineOfMatrix(matrix,0,counter)
        counter = countNumbersAroundSpecialCharsInLineOfMatrix(matrix,1,counter)
        #vypis_2D_pole(matrix)

    for line in sys.stdin:
        shiftMatrixUp(matrix, 1)
        addNextLineIntoMatrix(matrix, line)
        counter = countNumbersAroundSpecialCharsInLineOfMatrix(matrix,1,counter)
        #print("///////////////////////////////////")
        #vypis_2D_pole(matrix)
    
    print("END OF READING")    
    #count end of matrix
    vypis_2D_pole(matrix)
    
    addNextLineIntoMatrix(matrix, sys.stdin)
    print("///////////////////////////////////")
    vypis_2D_pole(matrix)
    
    for i in range(3):
        shiftMatrixUp(matrix, 1)
        print(repr(matrix[-1]))
        vypis_2D_pole(matrix)
        for x in range(len(matrix[-1])-1):
            matrix[-1][x]="."
            
        
        counter = countNumbersAroundSpecialCharsInLineOfMatrix(matrix,1,counter)
        i+=1

    
    ## poresene nacitani a posunovani dat.. ted jdes resit 
    ## testovani 1. radku a potom 2. a ostatnich az do konce vstupu, pak poresis posledni

        

refactor()

