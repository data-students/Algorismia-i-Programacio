import yogi

def digit_mes_frequent (llista: list[int], b: int) -> tuple[int, int]:
    '''Donada una llista i una base b, retorna el digit més freqüent d'aquella base i la quantitat de cops que ha sortit'''
    llista_frequencies = [0,0,0,0,0,0,0,0,0,0,0]
    
    for numero in llista:
        if numero == 0:
            llista_frequencies[0] += 1
        while numero > 0:
            digit = numero % b
            llista_frequencies[digit] += 1

            numero = numero // b

    maxima_frequencia = max(llista_frequencies)
    numero_maxima_frequencia = llista_frequencies.index(maxima_frequencia)
    return numero_maxima_frequencia, maxima_frequencia

def llegir_llista () -> list[int]:
    llista: list[int] = []
    entrada = yogi.scan(int)
    while entrada is not None:
        llista.append(entrada)
        entrada = yogi.scan(int)
    return llista

def main() -> None:
    base = yogi.read (int)
    llista = llegir_llista()
    numero, frequencia = digit_mes_frequent(llista, base)
    print (numero, frequencia)

if __name__ == "__main__":
    main()