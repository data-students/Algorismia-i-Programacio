import yogi

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True

def next_prime (n: int) -> int:
    if n == 2: # Únic nombre primer par
        return 3
    
    n += 2 # Com (quasi) tots els nombres primers son pars, ens estalviem la meitat de comprovacions

    while True:
        if is_prime (n):
            return n
        
        n += 2

def main () -> None:
    entrada = yogi.scan (int)

    while entrada is not None and is_prime (entrada):
        print (next_prime(entrada))
        
        entrada = yogi.scan (int)

if __name__ == "__main__":
    main()