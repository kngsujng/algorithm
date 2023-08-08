def solution(str_list, ex):
    return ''.join([str_list[i] for i, v in enumerate(str_list) if ex not in v])