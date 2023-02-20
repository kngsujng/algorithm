def solution(n):
    arr = [i for i in range(n, 0, -1) if n % i == 0]
    return len(arr)
            