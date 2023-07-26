def solution(my_string):
    arr=[]
    for i in my_string:
        try:
            arr.append(int(i))
        except:
            continue
    return sum(arr)