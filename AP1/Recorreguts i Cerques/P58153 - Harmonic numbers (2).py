import yogi

def interval_harmonic_number (n: int, m: int) -> float:
    resultat = 0.0
    
    for i in range (m+1,n+1):
        resultat += 1/i

    return resultat

def main() -> None:
    entrada1 = yogi.scan (int)
    entrada2 = yogi.scan (int)

    while entrada1 is not None and entrada2 is not None:
        print (f'{interval_harmonic_number(entrada1, entrada2):.010f}')

        entrada1 = yogi.scan (int)
        entrada2 = yogi.scan (int)

if __name__ == "__main__":
    main()