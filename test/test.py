import sys
from main import findSpecialCharsInInput

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

def test_findSpecialCharsInInput_noNumbersNoSpecialChars() -> None:
    specialChars= set()
    noSpecialChar={".","\r","\n"}
    specialChars = findSpecialCharsInInput()
    assert len(specialChars) == 0

