import yogi
from dataclasses import dataclass
from functools import cmp_to_key

@dataclass
class Player:
    name: str
    dtd: int      # número de doble triple-dobles
    td: int       # número de triple-dobles (que no són doble triple-doble)

def ordena_jugadores(p1: Player, p2: Player) -> int: 
    '''
    Post: Donades dues jugadores, retorna quina hauria d'estar per sobre de l'altra segons els 
    següents criteris: primer les que tinguin més dobles triple-dobles, en cas d'empat, les que 
    tinguin més triples-dobles (que no siguin dobles triple-dobles) i, si persisteix l'empat, 
    per ordre lexicogràfic del seu nom.
    '''
    if p1.dtd > p2.dtd:
        return -1
    elif p1.dtd < p2.dtd:
        return 1
    elif p1.td > p2.td:
        return -1
    elif p1.td < p2.td:
        return 1
    elif p1.name < p2.name:
        return -1
    else:
        return 1

def read_player(p: int) -> Player:
    '''
    Pre: p >= 0; a l'entrada hi ha un nom seguit de les seves estadístiques a p partits
    Post: retorna la informació d'una jugadora segons les dades que hi havia a l'entrada
    '''
    jugadora = Player(yogi.read(str), 0, 0)
    punts_partit = [[yogi.read(int) for _ in range(5)] for _ in range(p)]

    for partit in punts_partit:
        dtd = 0
        td = 0
        for puntuacio in partit:
            if puntuacio >= 20:
                dtd += 1
                td += 1
            elif puntuacio >= 10:
                td += 1
        if dtd >= 3:
            jugadora.dtd += 1
        elif td >= 3:
            jugadora.td += 1
    
    return jugadora

def main() -> None:
    p = yogi.read(int)
    n = yogi.read(int)
    if n > 0:
        llista_jugadores = [read_player(p) for _ in range(n)]
        llista_jugadores.sort(key=cmp_to_key(ordena_jugadores))
        for jugadora in llista_jugadores:
            print(jugadora.name, jugadora.dtd, jugadora.td, sep=" ")

if __name__ == "__main__":
    main()