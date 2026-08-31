import yogi

def magician_guesser(n: int) -> int:
    '''Donat un nombre n, retorna el "numero magic" original
    La fórmula original és la següent:
    n = ((((n * 5) + 6) * 4) + 9) * 5

    per tant, la formula inversa serà el resultat que retornarà aquesta funció
    '''
    
    resultat = ((((n // 5) - 9) // 4) - 6) // 5
    return resultat

def main():
    entrada = yogi.scan(int)
    while entrada is not None:
        print (magician_guesser (entrada))
        entrada = yogi.scan(int)

if __name__ == "__main__":
    main()