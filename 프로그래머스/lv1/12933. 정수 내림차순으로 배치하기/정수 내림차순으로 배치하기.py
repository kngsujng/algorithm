def solution(n):
    arr = [int(i) for i in str(n)]
    arr.sort(reverse=True)
    return int(''.join(str(i) for i in arr))