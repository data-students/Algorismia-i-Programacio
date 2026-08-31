import yogi
from typing import TypeAlias

Matriu: TypeAlias = list[list[int]]

def calcular_escales_permeses(matriu_vols: Matriu, a: int, b: int, c: int) -> list[int]:
    '''Retorna totes les escales que es poden fer per anar de la ciutat "a" a la ciutat "b" amb un cost igual o inferior a "c"
    utilitzant una matriu nxn de costos de tots els vols possibles.'''

    n = len(matriu_vols)
    escales_valides: list[int] = []
    for i in range(n):
        if matriu_vols[a][i] + matriu_vols[i][b] <= c:
            escales_valides.append(i)
    return escales_valides

def main() -> None:
    n = yogi.read(int)
    costos_vols = [[yogi.read(int) for _ in range(n)] for _ in range(n)]
    a = yogi.scan(int)
    while a is not None:
        b = yogi.read(int)
        c = yogi.read(int)
        escales_permeses = calcular_escales_permeses(costos_vols, a, b, c)

        print (f'{a} {b} {c}: ', end="")
        if escales_permeses == []:
            print ("res")
        else:
            print(f'{" ".join(str(x) for x in escales_permeses)}')

        a = yogi.scan(int)

if __name__ == "__main__":
    main()