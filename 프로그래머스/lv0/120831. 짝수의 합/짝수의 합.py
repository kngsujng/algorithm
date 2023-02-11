def solution(n):
    sum=0
    for n in range(1, n+1):
        if n % 2 == 0:
            sum += n
    return sum