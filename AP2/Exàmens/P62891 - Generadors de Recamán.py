from yogi import read, tokens
from typing import Iterator

def recaman(k: int) -> Iterator[int]:
    """Donat un natural k, genera la seqüència de Recamán amb paràmetre k."""

    an = n = 0 # Cas inicial
    aparicions = set() # Emmagatzemar les aparicions anteriors
    
    while True:
        yield an

        # Cálcul del següent terme
        n += 1
        condicio = an - n - k
        if condicio > 0 and condicio not in aparicions:
            an = condicio
        else:
            an = an + n + k
        
        # Afegir al conjunt d'aparicions anteriors
        aparicions.add(an)


def recaman_from(k: int, n: int) -> Iterator[int]:
    """Donat un natural k, genera la seqüència de 
    Recamàn amb paràmetre k."""

    seq = recaman(k)

    # Saltar-se els primers n termes de la seqüència
    for _ in range(n):
        next(seq)

    # Retornar els següents n termes
    while True:
        yield next(seq)


def recaman_first_completion(k: int, x: int) -> int:
    """Donat uns naturals k i x, retorna el primer n tal que {a0,...,an}
    conté tots els naturals fins a x ({0,...,x}). S'assumix que aquest valor 
    existeix, malgrat que aquest fet no ha estat encara mai demostrat."""
    
    seq = recaman(k)
    naturals = set(range(x + 1)) # Conjunt dels naturals {0...n}

    n = 0
    while True:
        an = next(seq)
        naturals.discard(an)
        if not naturals:
            return n
        n += 1

def main() -> None:
    """Programa principal"""

    for command in tokens(str):
        if command == "recaman":
            k, m = read(int), read(int)
            gen = recaman(k)
            print([next(gen) for _ in range(m)])
        elif command == "recaman_from":
            k, n, m = read(int), read(int), read(int)
            gen = recaman_from(k, n)
            print([next(gen) for _ in range(m)])
        elif command == "recaman_first_completion":
            k, x = read(int), read(int)
            print(recaman_first_completion(k, x))
        else:
            assert False


if __name__ == "__main__":
    main()