def solution(my_string, is_suffix):
    newArr = [my_string[i:] for i in range(len(my_string)-1, 0, -1)] + [my_string]
    return 1 if is_suffix in newArr else 0
    