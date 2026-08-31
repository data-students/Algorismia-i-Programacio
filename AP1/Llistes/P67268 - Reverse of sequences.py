import yogi

def imprimir_llista (L: list[int]) -> None:
    primer_numero = True
    for numero in L:
        if not primer_numero:
            print (end= " ")
        
        print (numero, end= "")
        primer_numero = False
        
def main() -> None:

    n = yogi.scan(int)
    while n is not None:
        llista: list[int] = []

        for _ in range (n):
            entrada = yogi.read(int)
            llista.append(entrada)

        llista.reverse()

        imprimir_llista (llista)
        print ()
        n = yogi.scan(int)

if __name__ == "__main__":
    main()