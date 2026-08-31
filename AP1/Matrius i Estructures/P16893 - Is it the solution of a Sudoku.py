from typing import TypeAlias
import yogi

Vector: TypeAlias = list[int]
Matrix: TypeAlias = list[Vector]

def te_tots_numeros (vector: Vector) -> bool:
    '''Donat un vector, retorn "True" si té tots els numeros (0-9). Retorna "False" alternament.'''
    for i in range (1, 10):
        if i not in vector:
            return False
    return True

def es_solucio (matriu: Matrix) -> bool:
    # Comprobar les files
    for i in range (9):
        if not te_tots_numeros(matriu[i]):
            return False
        
    # Comprobar columnes:
    for i in range (9):
        columna: Vector = []
        for j in range (9):
            columna.append(matriu[j][i])
        if not te_tots_numeros (columna):
            return False
    
    # Comprobar quadrats 3x3
    for i in range (3):
        quadrat: Vector = []
        for j in range (3): 
            for k in range (3):
                quadrat.append(matriu[3*i + k] [3*i + j])
        if not te_tots_numeros(quadrat):
            return False

        
    return True

def llegir_matriu() -> Matrix:
    '''Llegeix entrades d'enters i les emmagatzema com una matriu 9x9'''
    matriu: Matrix = []
    for _ in range (9):
        fila: Vector = []
        for _ in range (9):
            entrada = yogi.read(int)
            fila.append (entrada)
        matriu.append (fila)

    return matriu
    
def main() -> None:
    n = yogi.read(int)
    for _ in range (n):
        matriu = llegir_matriu()
        if es_solucio(matriu):
            print ("yes")
        else:
            print ("no")

if __name__ == "__main__":
    main()