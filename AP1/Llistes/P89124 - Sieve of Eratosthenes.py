import yogi

def sieve_eratosthenes (n: int) -> list [bool]:
    '''Retorna una llista de n+1 booleans on la posicio "i" diu si "i" és primer o no'''
    if n < 1:
        return [False]
    
    sieve = [True] * (n + 1)
    sieve [0] = False # El 0 NO és primer
    sieve [1] = False # El 1 NO és primer

    i = 0
    while i * i <= n:
        if sieve [i]:
            j = i * i
            while j <= n:
                sieve[j] = False
                j += i
        i += 1
    return sieve

def main () -> None:
    numero = yogi.scan (int)
    entrades: list[int] = []
    while numero is not None:
        entrades.append(numero)
        numero = yogi.scan(int)

    llista_primers = sieve_eratosthenes(max(entrades))

    for numero in entrades:
        if llista_primers[numero]:
            print (f'{numero} is prime')
        else:
            print (f'{numero} is not prime')



if __name__ == "__main__":
    main()