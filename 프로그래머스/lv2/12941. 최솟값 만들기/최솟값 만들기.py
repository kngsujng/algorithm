def solution(A,B):
    # 정확도 테스트는 통과지만, 효율성 테스트는 통과하지 못함
    # a = 0
    # A.sort()
    # B.sort()
    # for i in range(len(A)):
    #     a += A[0]*B[-1]
    #     A.remove(A[0])
    #     B.remove(B[-1])
    # return a
    
    a = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        a += A[0]*B[-1]
        A.pop(0)
        B.pop()
    return a