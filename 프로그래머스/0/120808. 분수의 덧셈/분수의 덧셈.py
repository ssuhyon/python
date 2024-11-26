def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    
    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return a
    
    gcd_value = gcd(numerator, denominator)
    numerator //=gcd_value
    denominator //=gcd_value
    answer = [numerator, denominator]
    return answer