def solution(my_string, n):
    my_list = list(my_string)
    arr = []
    for i in my_list:
        arr.append(i * n)
    return ''.join(arr)