def solution(n):
    arr = []
    while n != 1:
        arr.append(n)
        if n%2==0 :
            n//=2
        else:
            n=n*3+1
    return len(arr) if len(arr)<500 else -1