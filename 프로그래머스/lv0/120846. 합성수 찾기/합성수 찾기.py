def solution(n):
    arr = []
    for i in range(2, n+1):
        for j in range(1, i):
            if i%j == 0 and j!=1:
                arr.append(i)
    return len(list(set(arr)))
