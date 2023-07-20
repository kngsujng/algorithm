def solution(num_list):
    oddArr=[]
    evenArr=[]
    for i in num_list:
        if i%2==1:
            oddArr.append(i)
        else:
            evenArr.append(i)
    return [len(evenArr), len(oddArr)]