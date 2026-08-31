import yogi

def sequence_of_Collatz (n: int) -> int:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n*3 + 1
    
    return n

def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        nombre_de_passos = 0

        while entrada != 1:
            entrada = sequence_of_Collatz (entrada)
            nombre_de_passos += 1

        print (nombre_de_passos)
        
        entrada = yogi.scan(int)

if __name__ == "__main__":
    main()

