def solution(num_list, n):
    return [v for i, v in enumerate(num_list) if i % n == 0]