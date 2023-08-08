def solution(myString, pat):
    table = str.maketrans('AB','BA') #1대1대응
    myString = myString.translate(table)
    return int(pat in myString)
