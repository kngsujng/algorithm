def solution(x, n):
    arr=[]
    if x>0:
        for i in range(x, n*x+1, x):
            arr.append(i) 
    elif x<0:
        for i in range(x, n*x-1, x):
            arr.append(i) 
    else:
         return [0]*n  
    return arr