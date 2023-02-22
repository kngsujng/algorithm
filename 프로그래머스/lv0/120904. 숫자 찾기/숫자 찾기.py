def solution(num, k):
    numlist = [int(i) for i in str(num)]
    try:
        return numlist.index(k)+1
    except:
        return -1
