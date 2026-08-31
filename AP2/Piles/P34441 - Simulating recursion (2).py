import yogi
from typing import TypeAlias

Pila: TypeAlias = set[int]

def escriu(n: int) -> None:
    '''Donat un numero n, escriu en pantalla el patró
    recursiu de l'exercici demanat.'''

    pila = [n]
    while pila:
        actual = pila.pop()
        if actual > 1:
            pila.append(actual - 1)
            pila.append(actual)
            pila.append(actual - 1)
        else:
            print("", actual, end="")
            if pila:
                print("", pila.pop(), end="")
            if pila:
                print("", pila.pop(), end="")
            if pila:
                print("", pila.pop(), end="")
                

def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        escriu(entrada)
        print()
        entrada = yogi.scan(int)

if __name__ == "__main__":
    main()