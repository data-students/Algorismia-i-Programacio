import yogi

def llegir_llista () -> list[str]:
    llista: list[str] = []
    entrada = yogi.scan(str)
    while entrada is not None:
        llista.append(entrada)
        entrada = yogi.scan(str)
    return llista

def main() -> None:
    _ = yogi.read(int)

    entrades = llegir_llista()
    
    entrades.reverse()

    for paraula in entrades:
        print (paraula[::-1])

if __name__ == "__main__":
    main()