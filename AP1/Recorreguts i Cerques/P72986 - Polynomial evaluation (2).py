import yogi

def main() -> None:
    x = yogi.read(float)
    resultat = 0.0

    for entrada in yogi.tokens(float):
        resultat = entrada + resultat*x

    print (f'{resultat:.04f}')

if __name__ == "__main__":
    main()