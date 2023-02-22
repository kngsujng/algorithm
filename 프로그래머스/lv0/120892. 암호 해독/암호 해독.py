def solution(c, code):
    answer = ''
    for i in range(len(c)):
        if (i+1) % code == 0:
            answer += c[i]
    return answer