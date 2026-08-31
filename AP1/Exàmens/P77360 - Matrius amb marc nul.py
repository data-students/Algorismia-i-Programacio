import yogi
from typing import TypeAlias

Vector: TypeAlias = list[int]
Matrix: TypeAlias = list[Vector]

def te_marc_nul(matriu: Matrix) -> bool:

    files = len(matriu)
    columnes = len(matriu[0])
    sumes_acumulades = [[0 for _ in range(columnes + 1)] for _ in range(files + 1)]
    
    for i in range(1, files + 1):
        for j in range(1, columnes + 1):
            suma_acumulada = matriu[i - 1][j - 1] + sumes_acumulades[i - 1][j] + sumes_acumulades[i][j - 1] - sumes_acumulades[i - 1][j - 1]
            if suma_acumulada == 0:
                return True
            sumes_acumulades[i][j] = suma_acumulada

    return False

def llegir_matriu(m: int, n: int) -> Matrix:
    '''Llegeix un m * n elements i les disposa en una matriu m x n'''
    return [[yogi.read(int) for _ in range(n)] for _ in range(m)]

def main() -> None:
    m = yogi.read(int)
    n = yogi.read(int)
    matriu = llegir_matriu(m, n)
    print(te_marc_nul(matriu))
    
if __name__ == "__main__":
    main()