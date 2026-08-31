import yogi

def llegir_llista () -> list[int]:
    llista: list[int] = []
    entrada = yogi.scan(int) 
    while entrada is not None:
        llista.append(entrada - 1000000000)
        entrada = yogi.scan(int)
    return llista

def main() -> None:
    _ = yogi.read(int)
    llista_entrades = llegir_llista()
    llista_frequencies = [0] * 1001
    for numero in llista_entrades:
        llista_frequencies[numero] += 1

    for i in range (1001):
        frequencia = llista_frequencies[i]
        if frequencia != 0:
            print (f'{1000000000 + i} : {frequencia}')

if __name__ == "__main__":
    main()