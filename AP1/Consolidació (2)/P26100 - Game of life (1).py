from typing import TypeAlias
import yogi

Vector: TypeAlias = list[str]
Tauler: TypeAlias = list[Vector]

def estara_ocupat(tauler: Tauler, x: int, y: int) -> bool:
    '''Donat un tauler i una poscio (x,y) retorna "True" si es compleixen les condicions del joc de vida de Conway
    perquè aquella casella estigui ocupada per una bacteria. Retorna "False" alternament.'''

    bacteria_voltant = 0
    for i in range (-1, 2):
        for j in range (-1, 2):
            if (i != 0 or j != 0) and tauler[x + i] [y + j] == "B":
                bacteria_voltant += 1
    
    return (tauler[x][y] == "." and bacteria_voltant == 3) or (tauler[x][y] == "B" and (bacteria_voltant == 2 or bacteria_voltant == 3))

def seguent_t (tauler_ini: Tauler) -> Tauler:
    '''Donat un tauler inicial en temps t, retorna el tauler en el temps t + 1, seguint les regles del joc de la vida de Conway.'''

    tauler_fi: Tauler = []

    for i in range(len(tauler_ini) - 2):
        fila: Vector = []
        for j in range(len(tauler_ini[0]) - 2):
            if estara_ocupat(tauler_ini, i + 1, j + 1):
                fila.append("B")
            else:
                fila.append(".")
        tauler_fi.append(fila)
    
    return tauler_fi

def escriure_matriu(m: Tauler) -> None:
    '''Donada una matriu m, l'escriu, sense comes ni espais per files.'''
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="")
        print ()

def llegir_tauler(n: int, m: int) -> Tauler:
    
    sortida: Tauler = [['.'] * (m + 2)]
    for _ in range(n):
        fila: Vector = ['.']
        fila.extend(list(yogi.read(str)))
        fila.extend('.')
        sortida.append(fila)
    sortida.append (['.'] * (m + 2))

    return sortida

def main() -> None:
    es_primera = True
    n = yogi.scan(int)
    while n is not None:
        m = yogi.read(int)
        if n != 0 or m != 0:
            tauler_ini = llegir_tauler(n, m)
            tauler_fi = seguent_t(tauler_ini)
            if not (es_primera):
                print ()
            escriure_matriu(tauler_fi)
            es_primera = False

        n = yogi.scan(int)

if __name__ == "__main__":
    main()