import yogi

def nth_harmonic_number (n: int) -> float:
    resultat = 0.0
    for i in range (1,n+1):
        resultat += 1/i

    return resultat

def main() -> None:
    entrada = yogi.scan (int)

    while entrada is not None:
        print (f'{nth_harmonic_number(entrada):.04f}')
        entrada = yogi.scan (int)

if __name__ == "__main__":
    main()
