def solution(s):
    arr = list()
    for i in s.split(' '):
        if i.isalnum():
            arr.append(i[0].upper() + i[1:].lower())
        else:
            arr.append(i)
    return ' '.join(arr)