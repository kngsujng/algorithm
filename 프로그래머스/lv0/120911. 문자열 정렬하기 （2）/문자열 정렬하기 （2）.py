def solution(my_string):
    my_string = my_string.lower()
    arr = list(my_string)
    arr.sort()
    return ''.join(arr)