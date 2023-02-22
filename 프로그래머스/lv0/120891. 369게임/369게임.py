def solution(order):
    orderlist = map(int, str(order))
    arr = [i for i in orderlist if (i % 3 == 0) & (i != 0) ]
    return len(arr)
            