def solution(arr):
    Xarr = []
    for i in range(len(arr)):
        Xarr += [arr[i]] * arr[i]
    return Xarr