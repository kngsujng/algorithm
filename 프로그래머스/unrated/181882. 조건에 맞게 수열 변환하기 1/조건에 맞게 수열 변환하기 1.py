def solution(arr):
    newArr = []
    for i in arr:
        if i>=50 and i%2==0:
            newArr.append(i/2)
        elif i<50 and i%2==1:
            newArr.append(i*2)
        else:
            newArr.append(i)
    return newArr