import yogi
from typing import TypeAlias

Vector: TypeAlias = list[int]
Matrix: TypeAlias = list[Vector]

def llegir_matriu(n: int) -> Matrix:
    '''Llegeix una matriu nxn de nuemeros enters.'''

    matriu: Matrix = []
    for _ in range(n):
        fila: Vector = []
        for _ in range(n):
            entrada = yogi.read(int)
            fila.append(entrada)
        matriu.append(fila)

    return matriu

def es_quadrat_magic(matriu: Matrix) -> bool:
    '''Donada una matriu, retorna "True" si la matriu es un quadrat màgil. Retorna "False" alternament.'''
    # Guardar el "numero màgic", el valor que haurien de tenir totes les sumes de les files, coumnes i diagonals
    numero_magic = sum(matriu[0])
    llargada = len(matriu)

    # Comprovar la suma de les files
    for i in range(llargada):
        if sum(matriu[i]) != numero_magic:
            return False
        
    # Comprovar la suma de les columnes:
    for i in range(llargada):
        columna: Vector = [matriu[j][i] for j in range(llargada)]
        if sum(columna) != numero_magic:
            return False
    
    # Comprovar la suma de les diagonals:
    diagonal1: Vector = [matriu[i][i] for i in range(llargada)]
    if sum(diagonal1) != numero_magic:
        return False
    
    diagonal2: Vector = [matriu[i][llargada - (i + 1)] for i in range(llargada)]
    if sum(diagonal2) != numero_magic:
        return False
        
    # Si totes les comprovacions son satisfactòres...
    return True

def comprovar_numeros (matriu: Matrix) -> bool:
    '''Donada una matriu n x n, retorna "True" si surten tots els numeros entre 1 i n^2 exactament un cop.'''
    n = len(matriu)
    numeros = [False for _ in range(n*n)]
    for vector in matriu:
        for numero in vector:
            numeros[numero - 1] = True
    for i in numeros:
        if i == False:
            return False
    return True

def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        matriu = llegir_matriu(entrada)
        if entrada == 0 or not comprovar_numeros(matriu) or not es_quadrat_magic(matriu):
            print ("no")
        else:
            print ("si")

        entrada = yogi.scan(int)

if __name__ == "__main__":
    main()
