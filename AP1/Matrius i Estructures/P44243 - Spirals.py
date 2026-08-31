import yogi
from typing import TypeAlias

Vector: TypeAlias = list[str]
Matrix: TypeAlias = list[Vector]

def crear_matriu_punts(n: int) -> Matrix:
    '''Crea una matriu nxn de punts'''
    matriu: Matrix = []
    for _ in range(n):
        fila: Vector = []
        for _ in range(n):
            fila.append(".")
        matriu.append(fila)
    
    return matriu

def crear_espiral (matriu: Matrix) -> None:
    '''Donada una matriu nxn de punts la transforma en una espiral de X.'''
    llargada = len(matriu)
    if llargada == 1:
        matriu[:] = [["X"]]

    for i in range (llargada // 2):
        for j in range(2*i, llargada - 2*i):
            matriu[llargada - 1 - 2*i][j] = "X"
        for j in range(2*i, llargada - 2*i):
            matriu[llargada - j - 1][llargada - 1 - 2*i] = "X"
        for j in range (2*i, llargada - 1 - 2*i):
            matriu[2*i][llargada - j - 1] = "X"
        for j in range(2*i, llargada - 2 - 2*i):
            matriu [j][1 + 2*i] = "X"

def imprimir_matriu(matriu: Matrix) -> None:
    '''Escriu en pantalla una matriu donada.'''
    for i in range (len(matriu)):
        for j in range (len(matriu[0])):
            print (matriu[i][j], end=" ")
        print("")
    print("")

def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        if entrada != 0:
            matriu_punts = crear_matriu_punts (entrada)
            crear_espiral (matriu_punts)
            imprimir_matriu (matriu_punts)
        entrada = yogi.scan(int)

if __name__ == "__main__":
    main()