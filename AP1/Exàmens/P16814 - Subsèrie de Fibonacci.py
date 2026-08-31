import yogi

def seguent_fibo (fibo_n: int, fibo_n1: int) -> tuple [int, int]:
    '''Donats dons numeros de fibonacci f(n) i f(n-1), retorna f(n+1) (el seguent numero de fibonacci).'''
    return fibo_n + fibo_n1, fibo_n

def es_semifibo (n: int, fibo_n: int, fibo_n1: int) -> tuple[bool, int, int]:
    '''Retorna "True" si el nombre esta dins de la seqüència de fibonacci. Retorna "False" alternament.'''

    nombre_semifibo = False
    while n >= fibo_n:
        if n == fibo_n:
            nombre_semifibo = True
        
        fibo_n, fibo_n1 = seguent_fibo (fibo_n, fibo_n1)

    return nombre_semifibo, fibo_n, fibo_n1

def main () -> None:
    '''Es llegeix un seguit de números, si tots els numeros pertanyen a la sèrie de fibonacci, 
    retorna "True", sino retorn "False".'''

    entrada = yogi.scan(int)

    fibo_n = 1
    fibo_n1 = 0

    sequencia_semifibo = True

    while entrada is not None and sequencia_semifibo is True:
        resultat, fibo_n, fibo_n1 = es_semifibo (entrada, fibo_n, fibo_n1)
        if not resultat:
            sequencia_semifibo = False
        
        entrada = yogi.scan(int)

    if sequencia_semifibo:
        print ("yes")
    else:
        print ("no")

if __name__ == "__main__":
    main()