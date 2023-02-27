def solution(numbers):
    arr = []
    numbers.sort()
    for i in range(len(numbers)-1):
        for j in range(1, len(numbers)):
            print(numbers[i], numbers[j])
            arr.append(numbers[i]*numbers[j])
    return max(arr)