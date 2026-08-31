import yogi
from dataclasses import dataclass
from functools import cmp_to_key

@dataclass
class Paraula:
    nom: str
    frequencia: int

def ordena_llista_frequencies(p1: Paraula, p2: Paraula) -> int:
    if p1.frequencia > p2.frequencia:
        return -1
    elif p1.frequencia < p2.frequencia:
        return 1
    elif p1.nom < p2.nom:
        return -1
    else:
        return 1
    
def llegir_frequencia_entrades(n: int) -> list[Paraula]:
    '''Donat un numero n, llegeix n entrades i retorna la frequencia de les paraules que hi apareixen.'''
    llista_entrades = [yogi.read(str) for _ in range(n)]
    llista_entrades.sort()
    llista_frequencies: list[Paraula] = []
    i = 0
    frequencia = 0
    for j in range(n):
        if (j != 0 and llista_entrades[j] != llista_entrades[j - 1]):
            llista_frequencies.append(Paraula(llista_entrades[j - 1], frequencia))
            frequencia = 1
            i += 1
        else:
            frequencia += 1
    
    llista_frequencies.append(Paraula(llista_entrades[-1], frequencia))

    return llista_frequencies

def main() -> None:
    '''Programa principal'''
    n = yogi.scan(int)
    while n is not None:
        k = yogi.read(int)
        frequencia_entrades = llegir_frequencia_entrades(n)
        frequencia_entrades[:] = sorted(frequencia_entrades, key=cmp_to_key(ordena_llista_frequencies))
        for i in range(k):
            print (frequencia_entrades[i].nom)
        print ('-'*10)
        n = yogi.read(int)

if __name__ == "__main__":
    main()