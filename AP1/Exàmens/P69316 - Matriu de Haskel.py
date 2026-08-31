import yogi
from typing import TypeAlias

Vector:TypeAlias = list[int]
Matriu:TypeAlias = list[Vector]

def es_haskel(matriu: Matriu) -> bool:
    '''Donada una matriu m*m, retorna "True" si Ã©s una matriu de haskel, retorna "False" alternament.'''
    m = len(matriu)
    # Comprobar la part triangular superior:
    for i in range(m):
        const = matriu[0][i]
        for j in range(i + 1):
            actual = matriu[j][i-j]
            if actual != const:
                return False
            
    # Comprobar la part triangular inferior:
    for i in range(1, m):
        const = matriu[i][m - 1]
        for j in range(m - i):
            actual = matriu[i + j][m - j - 1]
            if  actual != const:
                return False

    return True
            

def main() -> None:
    n = yogi.read(int)
    for _ in range(n):
        m = yogi.read(int)
        matriu = [[yogi.read(int) for _ in range(m)] for _ in range(m)]
        if es_haskel(matriu):
            print('yes')
        else:
            print('no')    
    
if __name__ == "__main__":
    main()