import yogi
def imprimir_digit (n: int, base: int) -> None:

    digit = n % base
    print ("X" * digit)

    if n >= base:
        imprimir_digit (n // base, base)

def main():
    entrada = yogi.read(int)
    base = yogi.read(int)
    print ("-" * 10)
    imprimir_digit (entrada, base)
    print ("-" * 10)

if __name__ == "__main__":
    main()