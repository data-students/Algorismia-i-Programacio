import yogi

def equal_to_last (L: list[int], n: int) -> int:
    number = L[n - 1]
    repetitions = -1

    for numbers in L:
        if number == numbers:
            repetitions += 1
    if repetitions < 0:
        return 0
    
    return repetitions

def main() -> None:
    n = yogi.read(int)
    L: list[int] = []
    entrada = yogi.scan(int)
    while entrada is not None:
        L.append(entrada)
        entrada = yogi.scan(int)
    
    print (equal_to_last(L, n))

if __name__ == "__main__":
    main()