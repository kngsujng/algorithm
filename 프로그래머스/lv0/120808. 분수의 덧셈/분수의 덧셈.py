import fractions

def solution(numer1, denom1, numer2, denom2):
    for i in range(min(denom1, denom2), 0, -1):
        if denom1%i==0 and denom2%i==0:
            gcd=i
            break

    # 경우 1 : 최대공약수가 1이 아닐 때 
    if gcd!=1 :
        denom=denom1*(denom2//gcd)
        numer=numer1*(denom2//gcd)+numer2*(denom1//gcd)
        Irr = fractions.Fraction(denom, numer)
        return [Irr.denominator, Irr.numerator]
    # 경우 2 : 최대공약수가 1일 때 
    else:
        denom = denom1*denom2
        numer = numer1*denom2 + numer2*denom1
        Irr = fractions.Fraction(denom, numer)
        return [Irr.denominator, Irr.numerator]