import yogi

def main() -> None:
    suma = 0
    nombre_entrades = 0

    entrada = yogi.scan (float)
    while entrada is not None:
        suma += entrada
        nombre_entrades += 1
        entrada = yogi.scan(float)
    
    mitjana = suma / nombre_entrades
    
    print (f'{mitjana:.02f}')
        
if __name__ == "__main__":
    main()