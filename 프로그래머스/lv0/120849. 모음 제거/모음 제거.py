def solution(my_string):
    aeiou = "aeiou"
    arr = [i for i in my_string if aeiou.find(i) == -1]
    return ''.join(arr)