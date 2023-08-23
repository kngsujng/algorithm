def solution(s):
    minNum = str(min([int(i) for i in s.split(' ')]))
    maxNum = str(max([int(i) for i in s.split(' ')]))
    return minNum + ' ' + maxNum