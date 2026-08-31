def gcd2(a: int, b: int) -> int:

    if a > b:
        a, b = b, a

    while b != 0:
        r = a % b
        a = b
        b = r

    return a

def gcd4 (a: int, b: int, c: int, d: int) -> int:
    return gcd2(gcd2(a,b),gcd2(c,d))