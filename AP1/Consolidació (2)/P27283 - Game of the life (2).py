from typing import TypeAlias
import yogi

Vector: TypeAlias = list[str]
Tauler: TypeAlias = list[Vector]

def estara_ocupat(tauler: Tauler, x: int, y: int) -> bool:
    '''Donat un tauler i una poscio (x,y) retorna "True" si es compleixen les condicions del joc de vida de Conway
    perquè aquella casella estigui ocupada per una bacteria. Retorna "False" alternament.'''

    bacteria_voltant = 0
    n = len(tauler)
    m = len(tauler[0])
    for i in range (-1, 2):
        for j in range (-1, 2):
            # Assegurar-se de que les caselles del voltant existeixen
            if 0 <= x + i < n and 0 <= y + j < m and (i != 0 or j != 0):
                if (tauler[x + i] [y + j] == "B"):
                    bacteria_voltant += 1
    
    return (tauler[x][y] == "." and bacteria_voltant == 3) or (tauler[x][y] == "B" and (bacteria_voltant == 2 or bacteria_voltant == 3))

def seguent_t (tauler_ini: Tauler) -> Tauler:
    '''Donat un tauler inicial en temps t, retorna el tauler en el temps t + 1, seguint les regles del joc de la vida de Conway.'''

    tauler_fi: Tauler = []

    for i in range(len(tauler_ini)):
        fila: Vector = []
        for j in range(len(tauler_ini[0])):
            if estara_ocupat(tauler_ini, i, j):
                fila.append("B")
            else:
                fila.append(".")
        tauler_fi.append(fila)
    
    return tauler_fi

def escriure_matrius(matriu: list[Tauler]) -> None:
    '''Donada una llista de matrius, imprimeix aquestes matrius amb enters entre elles. Al final no s'imprimeix un enter.'''

    i = 0
    while i < len(matriu):
        matriz_str = "\n".join("".join(str(matriu[i][j][k]) for k in range(len(matriu[i][j]))) for j in range(len(matriu[i])))
        
        print(matriz_str)
        
        if i < len(matriu) - 1:
            print()
        
        i += 1

def main() -> None:
    '''Idea: Fer una llista amb tots els torns "t" i comprobar que no hi hagi un torn "t" que sigui exactament igual al torn "t - i".
    En cas de que ho sigui, tenim un bucle desde "i" fins a "t - 1".'''

    n = yogi.read(int)
    _ = yogi.read(int)

    tauler_t0 = [list(yogi.read(str)) for _ in range(n)]
    llista_bucles = [tauler_t0]
    final = False
    i = 0
    while not final:
        tauler_t1 = seguent_t(tauler_t0)
        i = len(llista_bucles) - 1
        while i >= 0 and not final:
            if tauler_t1 == llista_bucles[i]:
                final = True
            i -= 1
        llista_bucles.append(tauler_t1)
        tauler_t0 = tauler_t1

    escriure_matrius(llista_bucles[(i + 1):(len(llista_bucles) - 1)])

if __name__ == "__main__":
    main()