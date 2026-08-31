def prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def suma_xifres(n: int) -> int:
    suma = 0
    while n > 0:
        suma += n%10
        n = n//10
    return suma


def is_perfect_prime(n: int) -> bool:
    if n < 10:
        return prime(n)
    else:
        return is_perfect_prime(suma_xifres(n)) and prime(n)
