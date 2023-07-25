def solution(array, n): 
    newArr = [v for v in array if v != n]
    return len(array)-len(newArr)