def solution(n):
    for i in range(min(n, 6), 0, -1):
        if n%i==0 and 6%i==0:
            gdc = i
            break
    return n//gdc