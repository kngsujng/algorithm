def solution(s):
    lower = sorted([i for i in s if i.islower()], reverse=True)
    upper = sorted([i for i in s if i.isupper()], reverse=True)
    return ''.join(lower+upper)
