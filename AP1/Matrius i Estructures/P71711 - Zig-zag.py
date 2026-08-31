import yogi
from typing import TypeAlias

Vector: TypeAlias = list[int]
Matrix: TypeAlias = list[Vector]

def llegir_matriu(n: int, m: int) -> Matrix:
    '''Llegeix una matriu nxm de nuemeros enters.'''

    matriu: Matrix = []
    for _ in range(n):
        fila: Vector = []
        for _ in range(m):
            entrada = yogi.read(int)
            fila.append(entrada)
        matriu.append(fila)

    return matriu

def es_zig_zag(matriu: Matrix) -> bool:
    n = len(matriu[0])
    m = len(matriu)

    n_ant = matriu[0][0] - 1

    for col in range (n):
        if col % 2 == 0:
            for fila in range (m):
                n_act = matriu[fila][col]
                if n_act <= n_ant:
                    return False
                n_ant = n_act

        else:
            for fila in range (m - 1, -1, -1):
                n_act = matriu[fila][col]
                if n_act <= n_ant:
                    return False
                n_ant = n_act

    return True

def main() -> None:

    n = yogi.scan(int)
    contador_matrus = 1
    while n is not None:
        m = yogi.read(int)
        matriu = llegir_matriu(n, m)
        print (f'matriu {contador_matrus}:', end=" ")
        if n == 0 or m == 0 or not es_zig_zag (matriu):
            print("no")
        else: 
            print("yes")
            
        contador_matrus += 1
        n = yogi.scan(int)
        
if __name__ == "__main__":
    main()
