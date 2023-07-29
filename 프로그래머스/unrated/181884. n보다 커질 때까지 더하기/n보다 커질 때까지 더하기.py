def solution(numbers, n):
    sumArr = 0
    for i in numbers:
        sumArr+=i
        if sumArr > n:
            return sumArr
             