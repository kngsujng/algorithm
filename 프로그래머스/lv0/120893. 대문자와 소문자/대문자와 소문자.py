def solution(my_string):
    result = map(lambda x: x.lower() if x.isupper() else x.upper(), my_string)
    return ''.join(result)

            