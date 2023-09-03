def solution(numLog):
    arr = []
    for i in range(1, len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            arr.append('w')
        elif numLog[i] - numLog[i-1] == -1:
            arr.append('s')
        elif numLog[i] - numLog[i-1] == 10:
            arr.append('d')
        else: 
            arr.append('a')
    return ''.join(arr)