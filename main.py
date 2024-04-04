import sys
import re

matrix = []
activationChars= set()
#{'=', '&', '*', '-', '#', '$', '+', '%', '/', '@'}

def findSpecialChars(input:list):
    specialChars= set()
    noSpecialChar={".","\r","\n"}

    for y in input:            
        for x in y:
            if x in noSpecialChar:pass
            elif x.isdigit():pass
            else: specialChars.add(x)
    
    return specialChars

def checkForAlphabetCharsInInput(array:list):

    alphaCharsInInput = set()
    haveAlphaChars=False

    for line in array:            
        for lineChar in line:
            if lineChar.isalpha(): 
                haveAlphaChars=True
                print("Input has these alphabetical characters in it: " + repr(alphaCharsInInput))
    return haveAlphaChars

def fillMatrix():
    matrix = []
    inputChunk = []
    for line in sys.stdin:            
        for lineChar in line:
            if lineChar != "\r":
                inputChunk.append(lineChar)
            else: 
                matrix.append(inputChunk)
                inputChunk = []
                break
        #i+=1
    return matrix

def checkSpecialCharsAroundNumber(matrix: list, x, y, activationChars):
    specialCharAround = ""
    #top left corner
    if x==0 and y==0:
        try:
            # >
            if matrix[y][x+1] in activationChars:specialCharAround += "Right"
            # v
            if matrix[y+1][x] in activationChars:specialCharAround += "Down"
            # v->
            if matrix[y+1][x+1] in activationChars:specialCharAround += "Downright"
        except:
            print("expection at checking top left corner of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    #top mid line
    elif x > 0 and x < len(matrix[y])-1 and y==0:
        try:
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
        except:
            print("expection at checking top mid part of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    #top right corner
    elif x > 0 and x == len(matrix[y])-1 and y==0:
        try:
            # v
            if matrix[y+1][x] in activationChars:specialCharAround += "Down"
            # <-v
            if matrix[y+1][x-1] in activationChars:specialCharAround += "Downleft"
            # <
            if matrix[y][x-1] in activationChars:specialCharAround += "Left"
        except:
            print("expection at checking top right corner of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    #left mid column
    elif x == 0 and y>0 and y < len(matrix)-1:
        try:
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
        except:
            print("expection at checking left column of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    
    #mid mid
    elif x > 0 and y>0 and y < len(matrix)-1 and x<len(matrix[y])-1:
        try:
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
        except:
            print("expection at checking mid part of matrix. Coor: [" + str(x) + "," + str(y) + "]")

    #right mid column
    elif x < len(matrix[y])-1 and y>0 and y < len(matrix)-1:
        try:
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
        except:
            print("expection at checking right column of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    
    #down left corner
    if x==0 and y== len(matrix)-1:
        try:
            # >
            if matrix[y][x+1] in activationChars:specialCharAround += "Right"
            # ^
            if matrix[y-1][x] in activationChars:specialCharAround += "Top"
            # ^->
            if matrix[y-1][x+1] in activationChars:specialCharAround += "Topright"
        except:
            print("expection at checking top left corner of matrix. Coor: [" + str(x) + "," + str(y) + "]")

    #down mid line
    elif x > 0 and x < len(matrix[y])-1 and y==len(matrix)-1:
        try:
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
        except:
            print("expection at checking bottom mid corner of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    
    #down right corner
    if x==len(matrix[y])-1 and y== len(matrix)-1:
        try:
            # <
            if matrix[y][x-1] in activationChars:
                specialCharAround += "Left"
            # ^
            if matrix[y-1][x] in activationChars:
                specialCharAround += "Top"
            # <-^
            if matrix[y-1][x-1] in activationChars:
                specialCharAround += "Topleft"
        except:
            print("expection at checking bottom right corner of matrix. Coor: [" + str(x) + "," + str(y) + "]")
    return specialCharAround

def print_2D_List(array):
  for line in array:
    for char in line:
      print(f"{char:2}", end="")
    print()

def countNumbersAroundSpecCharsIn2DArray(ar):
    counter=0
    countNumber=False
    numberToConvert=""

    activationChars =  findSpecialChars(ar)
    

    if checkForAlphabetCharsInInput(ar): 
        print("input has characters in it - abborting")
        return 0



    for y in range(len(ar)):
        for x in range(len(ar[y])):
            #DEBUG 
            # if str(ar[y][x])!="." : print("coor: [" + str(x) + "," + str(y) + "] = "+ str(ar[y][x]))
            if str(ar[y][x]).isdigit():
                try:
                    specChar=checkSpecialCharsAroundNumber(ar,x,y, activationChars)
                except:
                    print("There is problem with checking special chars at : coor: [" + str(x) + "," + str(y) + "]")
                specChar=checkSpecialCharsAroundNumber(ar,x,y, activationChars)
                if len(specChar)>0: countNumber=True
                numberToConvert+=str(ar[y][x])
                if x+1<len(ar[y]) and str(ar[y][x+1]).isdigit():
                    pass
                elif x==len(ar[y]) and y ==len(ar):
                    counter+=int(numberToConvert)
                    numberToConvert=""
                    specChar=""
                    countNumber=False
                else:
                    if countNumber:
                        #DEBUG - make counted numbers bunch of zeros
                        """ 
                        for z in range(len(numberToConvert)):
                            ar[y][x-z]=0 """

                        counter+=int(numberToConvert)
                        numberToConvert=""
                        specChar=""
                        countNumber=False
                        #DEBUG
                        #print("counter = " + str(counter))
                    else:
                        numberToConvert=""
                        specChar=""
                        #DEBUG 
                        #print("number wasnt around special char")
    return counter

matrix = fillMatrix()
print(countNumbersAroundSpecCharsIn2DArray(matrix))




