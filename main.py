import sys
import re

matrix = []

activationChars = set()

def findSpecialCharsInInput():
    specialChars= set()
    noSpecialChar={".","\r","\n"}

    for line in sys.stdin:            
        for lineChar in line:
            if lineChar in noSpecialChar:pass
            elif lineChar.isdigit():pass
            else: specialChars.add(lineChar)
    
    return specialChars

def fillMatrix():
    i=0
    inputChunk = []
    for line in sys.stdin:
        if i < 2: #TODO remove when want to solve full problem
            print(repr(line))
            
            for lineChar in line:
                if lineChar != "\r":
                    inputChunk.append(lineChar)
                else: 
                    print("ELSE ______________________")
                    print(inputChunk)
                    matrix.append(inputChunk)
                    inputChunk = []
                    break
            i+=1

#deprecated
def firstRowSolve(line,matrix):
    numberToCastToInt=""
    countNumber=False
    for i in matrix[line][i]:
        if i == ".": #no char
            pass

        elif i.isdigit(): #number
            if True:
            numberToCastToInt += matrix[line][i]

            if matrix[i+1].isdigit():
                
                pass
            else:
                countNumber=True

        else: #special char
            pass


    pass

def checkTop(matrix, x, y):
    pass
def checkLeft(matrix, x, y):
    pass
def checkBottom(matrix, x, y):
    pass
def checkRight(matrix, x, y):
    pass

def checkSpecialCharsAroundNumber(matrix, x, y):
    
    #top left corner
    if x==0 and y==0:
        # >
        if matrix[x+1][y] in activationChars:return True
        # v
        if matrix[x][y+1] in activationChars:return True
    #top mid line
    elif x > 0 and x < len(matrix[x]) and y==0:
        pass
    #top right corner
    elif x > 0 and x == len(matrix[x])-1 and y==0:
        pass
    #left mid 
    elif x==0 and y > 0 and y < len(matrix)-1:
        pass
    #mid
    elif x > 0 and x < len(matrix)-1 and y > 0 and y < len(matrix)-1:
        pass
    #right mid 
    elif x == len(matrix)-1 and y > 0 and y < len(matrix)-1:
        pass
    #bot left
    elif x == 0 and y == len(matrix)-1:
        pass

    #bot mid
    elif x > 0 and x < len(matrix)-1 and y == len(matrix)-1:
        pass

    #bot right
    elif x == len(matrix)-1 and y == len(matrix)-1:
        pass


def solve():
    fillMatrix()

    counter=0
    
    i=0
    for i in range(matrix):

        if firstRow:
            firstRowSolve(i, matrix)
            firstRow=False
        



        if lastRow:
            pass



    


fillMatrix()

print("\n KONEC")
print(matrix[0][2])


