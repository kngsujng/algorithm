def solution(arr):
    return min([int(arr[i][j] == arr[j][i]) for i in range(len(arr)) for j in range(len(arr))])
            