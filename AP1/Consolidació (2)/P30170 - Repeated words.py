'''Feu un programa que, donada una seqüència de paraules, calculi quants caràcters tenen en total les paraules que apareixen 1 cop, quants caràcters tenen en total les paraules que apareixen 2 cops, quants caràcters tenen en total les paraules que apareixen 3 cops, etcètera.

Entrada

L’entrada consisteix en diversos casos. Cada cas comença amb un nombre 1 ≤ n ≤ 105, seguit de n paraules.

Sortida

Per a cada cas d’entrada i per a cada nombre x de repeticions, escriviu en una línia la quantitat total de caràcters (no comptant les repeticions) de les paraules que apareixen exactament x cops. Si no hi hagués cap paraula amb x repeticions, no escrigueu res per a aquesta x. Escriviu una línia buida després de cada cas.'''

import yogi
from dataclasses import dataclass
from functools import cmp_to_key

@dataclass
class Paraula:
    nom: str
    frequencia: int

def escriu_lletres_per_frequencies(llista_frequencies: list[Paraula]) -> None:

    comptador_lletres = 0
    frequencia_anterior = llista_frequencies[0].frequencia
    for paraula in llista_frequencies: 
        if paraula.frequencia != frequencia_anterior:
            print (f'{frequencia_anterior} : {comptador_lletres}')
            comptador_lletres = len(paraula.nom)
        else:
            comptador_lletres += len(paraula.nom)
        frequencia_anterior = paraula.frequencia
    
    print (f'{frequencia_anterior} : {comptador_lletres}')

def ordena_frequencies(paraula1: Paraula, paraula2: Paraula) -> int:

    return paraula1.frequencia - paraula2.frequencia

def crear_llista_frequencies(n: int) -> list[Paraula]:

    llista_entrades = [yogi.read(str) for _ in range(n)]
    llista_frequencies: list[Paraula] = []
    llista_entrades.sort()
    paraula_anterior = llista_entrades[0]
    for paraula in llista_entrades:
        if llista_frequencies == [] or paraula != paraula_anterior:
            llista_frequencies.append(Paraula(paraula, 1))
        else:
            llista_frequencies[-1].frequencia += 1
        paraula_anterior = paraula

    return llista_frequencies

def main() -> None:
    n = yogi.scan(int)
    while n is not None:
        llista_frequencies = crear_llista_frequencies(n)
        llista_frequencies.sort(key=cmp_to_key(ordena_frequencies))
        escriu_lletres_per_frequencies(llista_frequencies)
        print()
        n = yogi.scan(int)

if __name__ == "__main__":
    main()