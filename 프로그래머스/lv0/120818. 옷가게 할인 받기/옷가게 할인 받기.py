def solution(price):
    if price>=500000:
        return int(price*(1-0.2))
    elif price>=300000:
        return int(price*(1-0.1))
    elif price>=100000:
        return int(price*(1-0.05))
    else:
        return price
    # print(int(round(11111*(1-0.2), -1)))