def solution(s):
    s = s.lower()
    parr = [i for i in s if i=="p" in s]
    yarr = [i for i in s if i=="y" in s]
    if len(parr) == len(yarr):
        return True
    else:
        return False