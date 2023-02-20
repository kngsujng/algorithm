def solution(age):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    n_list = list(map(int, str(age)))
    return ''.join(alph[i] for i in n_list)