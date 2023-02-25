def solution(numbers):
    arr=[]
    for i in range(0,10):
        if i not in numbers:
            arr.append(i)
    return sum(arr)