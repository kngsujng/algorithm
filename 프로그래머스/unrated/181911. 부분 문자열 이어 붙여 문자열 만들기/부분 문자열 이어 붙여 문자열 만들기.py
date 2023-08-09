def solution(my_strings, parts):
    answer = ''
    for idx in range(len(my_strings)):
        a, b = parts[idx]
        answer+=my_strings[idx][a:b+1]
    return answer