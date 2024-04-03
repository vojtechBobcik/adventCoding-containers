import sys
import re

matrix = []

activationChars= {'=', '&', '*', '-', '#', '$', '+', '%', '/', '@'}


def vypis_pole(pole):
  for radek in pole:
    for sloupec in radek:
      print(f"{sloupec:2}", end="")
    print()

def findSpecialCharsInInput():
    specialChars= set()
    noSpecialChar={".","\r","\n"}

    for line in sys.stdin:            
        for lineChar in line:
            if lineChar in noSpecialChar:pass
            elif lineChar.isdigit():pass
            else: specialChars.add(lineChar)
    
    return specialChars

def findSpecialChars(input):
    specialChars= set()
    noSpecialChar={".","\r","\n"}

    for y in input:            
        for x in y:
            if x in noSpecialChar:pass
            elif x.isdigit():pass
            else: specialChars.add(x)
    
    return specialChars

def checkForAlphabetCharsInInput():
    alphaChars= set()

    for line in sys.stdin:            
        for lineChar in line:
            if lineChar.isalpha(): alphaCharsInInput=True
    
    return alphaChars

def fillMatrix():
    matrix = []
    #i=0
    inputChunk = []
    for line in sys.stdin:
        #if i < 5: #TODO remove when want to solve full problem
            #print(repr(line))
            
        for lineChar in line:
            if lineChar != "\r":
                inputChunk.append(lineChar)
            else: 
                #print("ELSE ______________________")
                #print(inputChunk)
                matrix.append(inputChunk)
                inputChunk = []
                break
        #i+=1
    return matrix

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




def countNumbersAroundSpecCharsIn2DArray(ar):
    counter=0
    countNumber=False
    numberToConvert=""
    
    for y in range(len(ar)):
        
        
        for x in range(len(ar[y])):
            
            if str(ar[y][x])!="." : print("coor: [" + str(x) + "," + str(y) + "] = "+ str(ar[y][x]))
            if ar[y][x].isdigit():
                specChar=checkSpecialCharsAroundNumber(ar,x,y)
                if len(specChar)>0: countNumber=True
                numberToConvert+=str(ar[y][x])
                if x+1<len(ar[y]) and ar[y][x+1].isdigit():
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
                        #print("number wasnt around special char") """
    return counter
        
def addLineIntoMatrix(workingArray, inputLine):
    
    inputChunk = []
    ar=workingArray
  
    if len(ar) < 3:
        for lineChar in inputLine:
            #TODO work with EOF one line
            if lineChar != "\r":
                inputChunk.append(lineChar)
            else:  
                ar.append(inputChunk)
                #debug
                print("_________________________________________" + str(len(ar)))
                vypis_pole(ar)
                inputChunk = []
                break
    
    else:
        print("else")
        print(inputLine)
        for lineChar in inputLine:
            if lineChar != "\r":
                inputChunk.append(lineChar)
            else:
                print("_________________________________________" + str(len(ar)))
                print("else else")
                print()
                print(inputChunk)
                vypis_pole(ar)
                ar[0]=ar[1]
                ar[1]=ar[2]
                ar[2]=inputChunk
                print("_________________________________________")
                vypis_pole(ar)
                
                
                inputChunk=[]
    workingArray = ar
    return workingArray

def solveLine(line):
    
    for x in range(len(line)):
            
            if str(line[x])!="." : print("coor: [" + str(x) + "," + str(y) + "] = "+ str(line[x]))
            if line[x].isdigit():
                specChar=checkSpecialCharsAroundNumber(ar,x,y)
                if len(specChar)>0: countNumber=True
                numberToConvert+=str(line[x])
                if x+1<len(line) and line[x+1].isdigit():
                    pass
                elif x==len(line) and y ==len(ar):
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
                            line[x-z]=0

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

def refactor():
    matrix = []
    
    for line in sys.stdin:
        addLineIntoMatrix(matrix, line)
        

#matrix = fillMatrix()

refactor()

