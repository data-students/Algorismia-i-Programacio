import yogi

def parells(m: int, llista: list[int]) -> int:
    '''
    Post: Donada una llista d'enters, retorna quants parells d'elements 
    xi i xj (amb i ≠ j) té tals que xi + xj és un múltiple de m.
    '''
    nre_parells = 0
    for i in range(len(llista) - 1):
        for j in range(i + 1, len(llista)):
            if i != j and (llista[i] + llista[j]) % m == 0:
                nre_parells += 1
    return nre_parells

def main() -> None:
    m = yogi.scan(int)
    while m is not None:
        n = yogi.read(int)
        entrades = [yogi.read(int) for _ in range(n)]
        print(parells(m, entrades))
        m = yogi.scan(int)

if __name__ == "__main__":
    main()
