def solution(phone_number):
    if len(phone_number) > 4:
        for i in phone_number[:-4]:
            return "*" * len(phone_number[:-4]) + phone_number[-4:]
    else:
        return phone_number

    
    