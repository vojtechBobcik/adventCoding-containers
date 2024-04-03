import sys


activationChars= {'=', '&', '*', '-', '#', '$', '+', '%', '/', '@'}


testArray = [
    ['2','3','3','#'],
    ['.','.','.','.'],
    ['#','.','.','.'],
    ['2','2','.','.'],
    ['#','.','.','.'],
    ['.','.','#','.'],
    ['2','2','#','3']
]

specialCharTestArray = [
    ['2','3','3','#'],
    ['.','.','.','.'],
    ['*','.','.','.'],
    ['2','2','.','.'],
    ['@','.','.','.'],
    ['.','.','%','.'],
    ['2','2','#','3']
]

noSpecialCharTestArray = [
    ['2','3','3','.'],
    ['.','3','.','.'],
    ['.','.','2','2'],
    ['.','.','.','.'],
    ['.','1','.','.'],
    ['.','.','0','.'],
    ['2','2','.','3']
]

noNumberTestArray = [
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.']
]

""" def test_findSpecialCharsInInput_noNumbersNoSpecialChars() -> None:
    specialChars= set()
    noSpecialChar={".","\r","\n"}
    specialChars = findSpecialCharsInInput()
    assert len(specialChars) == 0 """

def test():

    for i in range(3):
        for lineChar in sys.stdin.readline():
            #debug
            print(repr(lineChar))
        i+=1
        
test()
