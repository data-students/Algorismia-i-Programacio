import yogi

def viatje_valid(ciutats: list[int], diposit_maxim: int, s: int) -> bool:

    diposit_actual = diposit_maxim
    i = 0
    while i < len(ciutats):
        diposit_actual -= ciutats[i]
        if diposit_actual < 0:
            i -= 1
            diposit_actual = diposit_maxim
            s -= 1
            if s < 0:
                return False
        i += 1
    return True

def calcula_diposit_minim(ciutats: list[int], s: int) -> int:
    '''Utilitza cerca binària per "optimitzar" l'autonomia minima que necessita un cotxe fent <= s parades'''
    esq = max(ciutats) # diposit minim
    dre = sum(ciutats) # diposit màxim

    while esq < dre:
        mid = (esq + dre) // 2
        if viatje_valid(ciutats, mid, s):
            dre = mid
        else:
            esq = mid + 1

    return esq

def main() -> None:

    for n in yogi.tokens(int):
        s = yogi.read(int)
        ciutats = [yogi.read(int) for _ in range(n)]
        print(calcula_diposit_minim(ciutats, s))

if __name__ == "__main__":
    main()
