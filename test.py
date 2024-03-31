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
        if matrix[y][x+1] in activationChars:specialCharAround += "Right"
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
         # v->
        if matrix[y+1][x+1] in activationChars:specialCharAround += "Downright"
    #top mid line
    elif x > 0 and x < len(matrix[x])-1 and y==0:
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
    elif x > 0 and x == len(matrix[x])-1 and y==0:
        # v
        if matrix[y+1][x] in activationChars:specialCharAround += "Down"
        # <-v
        if matrix[y+1][x-1] in activationChars:specialCharAround += "Downleft"
        # <
        if matrix[y][x-1] in activationChars:specialCharAround += "Left"
    return specialCharAround


def vypis_pole(pole):
  """
  Funkce vypíše dvourozměrné pole na konzoli.

  Argumenty:
    pole: Dvourozměrné pole.
  """
  for radek in pole:
    for sloupec in radek:
      print(f"{sloupec:2}", end=" ")
    print()

y=0

ar = [
    ['2','3','3','#'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['2','2','.','.'],
]
counter=0
countNumber=False
numberToConvert=""
for x in range(len(ar[y])):
    
    print(ar[y][x])

    if ar[y][x].isdigit():

        specChar=checkSpecialCharsAroundNumber(ar,x,y)
        print("[" + str(x) + "," + str(y) + "] - " +  specChar)

        if len(specChar)>0: countNumber=True
        numberToConvert+=str(ar[y][x])

        if ar[y][x+1].isdigit():
            pass
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
            else:
                print("number wasnt around special char")

                
vypis_pole(ar)


    
