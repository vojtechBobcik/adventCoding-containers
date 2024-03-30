import sys
import re

matrix = []

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

def firstRowSolve(row):
    numberToCast=""
    countNumber=False
    for i in row:
        if i == ".": #no char
            pass

        elif i.isdigit(): #number
            numberToCast += row[i]

            if row[i+1].isdigit():
                pass

        else: #special char
            pass


    pass


def solve():
    fillMatrix()

    firstRow=True
    lastRow=False
    firstChar=True
    lastChar=False

    counter=0
    
    i=0
    for i in range(matrix):

        if firstRow:
            firstRowSolve(matrix)
            firstRow=



        if lastRow:
            pass



    


fillMatrix()

print("\n KONEC")
print(matrix[0][2])


