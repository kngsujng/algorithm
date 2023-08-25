def solution(n, m):
    gcb = max(i for i in range(max(n,m), 0, -1) if m%i == 0 and n%i == 0)
    lcm = gcb * (m//gcb) * (n//gcb)
    return [gcb, lcm]
        