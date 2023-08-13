def solution(s):
    return len([i for i in s.lower() if i=='p']) == len([i for i in s.lower() if i=='y'])
