def gcd(a: int, b: int) -> int:

    if a > b:
        a, b = b, a

    while b != 0:
        r = a % b
        a = b
        b = r

    return a
