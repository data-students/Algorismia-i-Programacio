import yogi

def work(n: int) -> None:
    '''Donat un nombre n, escriu en pantalla el
    patró recursiu demanat pel exercici.'''

    pila = [n]

    while pila:
        actual = pila.pop()
        if actual > 0:
            print("", actual, end="")
            pila.append(actual - 1)
            pila.append(actual - 1)
    print()

def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        work(entrada)
        entrada = yogi.scan(int)

if __name__ == "__main__":
    main()