def solution(s1, s2):
    arr=[]
    for i in s1:
        for j in s2:
            if i==j:
                arr.append(i)
    return len(arr)
