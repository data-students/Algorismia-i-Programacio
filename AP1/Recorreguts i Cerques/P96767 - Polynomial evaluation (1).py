import yogi

def main() -> None:
    x = yogi.read (float)
    resultat = 0

    grau_x = 0
    for coeficient in yogi.tokens(float):
        resultat += coeficient* (x**grau_x)
        grau_x += 1
    
    print (f'{resultat:.04f}')

if __name__ == "__main__":
    main()