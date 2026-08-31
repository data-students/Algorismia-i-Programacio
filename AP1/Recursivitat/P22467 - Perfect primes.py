def is_prime (n: int) -> bool:
    '''Donat un numero n, retorna "True" si n es primer i "False" alternament.'''
    if n < 2:
        return False
    if n == 2:
        return True
    
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


def is_perfect_prime(n: int) -> bool:
    '''
    Donat un nombre n, retorna "True" si n és primer i la seqüencia de totes les sumes dels 
    seus digits també son primers. Retorna "False" alternament.
    '''

    n_is_prime = is_prime(n)

    if not n_is_prime or n <= 10:
        return n_is_prime
    
    else:
        nStr = str(n)
        suma = 0

        for digit in nStr:
            suma += int(digit)

        if is_prime(suma):
            return (is_perfect_prime(suma))
        else:
            return False