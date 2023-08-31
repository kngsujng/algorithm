def solution(s):
    a=[]
    arr = s.split(' ')
    for i in arr:
        a.append(''.join([val.upper() if idx%2==0 else val.lower() for idx, val in enumerate(i)]))
    return ' '.join(a)
    # s = '   asd  asdf '
    # a = s.strip()
    # a = s.replace(' ', '/')
    # return ''.join([v.upper() if i%2==0 else v.lower() for i, v in enumerate(a)])