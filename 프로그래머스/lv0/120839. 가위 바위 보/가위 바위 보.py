def solution(rsp):
    li_rsp = list(rsp)
    answer = []
    for i in li_rsp:
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        else:
            answer.append('2')
    return ''.join(i for i in answer)