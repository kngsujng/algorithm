def solution(my_string, index_list):
    answer = ''
    for j in index_list:
        for i, v in enumerate(my_string):
            if i == j:
                answer+=v
    return answer