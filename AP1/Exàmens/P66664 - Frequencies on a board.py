import yogi
from dataclasses import dataclass
from typing import TypeAlias

Vector: TypeAlias = list[int]
Matrix: TypeAlias = list[Vector]

def compta_frequencies(matriu: Matrix) -> Matrix:
    '''Donada una matriu m x n, retorna el nombre de vegades que surt
    cada numero per columnes.'''

    m = len(matriu)
    n = len(matriu[0])
    frequencies = [[0 for _ in range(n)] for _ in range(10)]

    for j in range(n):
        for i in range(m):
            frequencies[matriu[i][j]][j] += 1

    return frequencies

def escriure_matriu(matriu: Matrix) -> None:
    '''Donada una matriu, l'escriu en format en pantalla.'''
    for fila in matriu:
        print(" ".join(str(element)for element in fila))
    print()

def main() -> None:
    m = yogi.scan(int)
    while m is not None:
        n = yogi.read(int)
        matriu = [[yogi.read(int) for _ in range(n)] for _ in range(m)]
        frequencies = compta_frequencies(matriu)
        escriure_matriu(frequencies)
        m = yogi.scan(int)

if __name__ == "__main__":
    main()
