def solution(left, right):
    answer=list()
    for num in range(left, right+1):
        arr = [i for i in range(1, num+1) if num%i==0]
        if len(arr)%2==0:
            answer.append(num)
        else:
            answer.append(-num)
    return sum(answer)