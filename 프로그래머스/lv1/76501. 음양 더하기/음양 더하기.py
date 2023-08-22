def solution(absolutes, signs):
    positive = [num for sign, num in zip(signs, absolutes) if sign]
    negative = [num for sign, num in zip(signs, absolutes) if not sign]
    return sum(positive)-sum(negative)
            