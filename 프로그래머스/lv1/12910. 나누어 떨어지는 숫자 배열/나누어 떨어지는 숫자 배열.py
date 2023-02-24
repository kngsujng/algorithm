def solution(arr, divisor):
    arr = [i for i in arr if i%divisor==0]
    arr.sort()
    if len(arr)==0:
        arr=[-1]
    return arr