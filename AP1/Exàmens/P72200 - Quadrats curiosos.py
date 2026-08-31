import yogi

def quadrats_curiosos (numero: int, nivell: int) -> None:
    '''Funcio que escriu un quadrat xxn segons els patró dels exemples'''
    # Cas base quan nivell = 0: No fer res

    # Cas inductiu:
    if nivell > 0:
        posicio = numero
        n = (nivell - 1) % 10

        # Aqui s'escriu el patró del mateix nuemero repetit
        while posicio > nivell:
            print (n, end="")
            posicio -= 1
            
        # Aqui s'escriu el patró dels nombres decreixents del 9 al 0
        while posicio != 0:
            print (n, end="")
            posicio -= 1
            if n == 0:
                n = 10
            n -= 1

        # En cas de que el número que s'escriu és 0, es posa de nou perquè el pròxim nivell ho faci des del 9.
        if numero == 0:
            numero = 10
        
        # S'escriu un salt de linea entre nivell i nivell
        print()

        # Es repeteix el cicle per un nivell menys fins que arribem al 0
        quadrats_curiosos (numero, nivell - 1)
    
def main() -> None:
    es_primera_entrada = True
    for entrada in yogi.tokens(int):

        # Separem dos quadrats consecutius amb una línea buida. El primer quadrat no s'ha de separar amb aquesta linea buida.
        if not es_primera_entrada:
            print ()

        quadrats_curiosos (entrada, entrada)
        es_primera_entrada = False


if __name__ =="__main__":
    main()