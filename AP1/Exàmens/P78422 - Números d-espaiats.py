import yogi

def d_espaiats (base: int, d: int, n: int, solucions: int) -> bool:
    '''Donat un numero n i una base b, retorna "True" si aquest número és un numero d-espaiat. Retorna "False" alternament.'''
    if n < (base):
        return True
    
    digit1 = n % base
    digit2 = (n // base) % base

    if digit1 == d or digit2 == d:
        return d_espaiats(base, d, n // base, solucions)
    
    return False

def main() -> None:
    base = yogi.scan(int)

    while base is not None:
        solucions = 0
        d = yogi.read(int)
        sequencia = yogi.read(int)

        for _ in range(sequencia):
            n = yogi.read(int)
            if d_espaiats(base, d, n, 0):
                solucions += 1
        
        print (solucions)
        base = yogi.scan(int)

if __name__ == "__main__":
    main()