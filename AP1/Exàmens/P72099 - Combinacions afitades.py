import yogi

def escriu_combinacions(p: int, n: int, k: int, combinacio: list[int], i: int, suma: int) -> None:
    '''
    Escriu en ordre ascendent, totes les combinacions de mida p, a partir de la posició d'una combinació
    inicial dels primers n números senars tals que la seva suma sigui més petita o igual que k.
    '''

    if i >= p and suma <= k:
        print(" ".join(str(element) for element in combinacio))
    else:
        for j in range(1, 2*n, 2):
            if suma + j <= k:
                combinacio[i] = j
                escriu_combinacions(p, n, k, combinacio, i + 1, suma + j)

def main() -> None:
    p = yogi.scan(int)
    while p is not None:
        n = yogi.read(int)
        k = yogi.read(int)

        escriu_combinacions(p, n, k, [0 for _ in range(p)], 0, 0)
        print("-" * (2*p - 1))

        p = yogi.scan(int)

if __name__ == "__main__":
    main()
