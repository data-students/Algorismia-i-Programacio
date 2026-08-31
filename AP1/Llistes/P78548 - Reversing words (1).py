import yogi

def main() -> None:
    entrada = yogi.scan(str)
    while entrada is not None:
        entrada_invertida = entrada[::-1]
        print (entrada_invertida)
        entrada = yogi.scan(str)
        
if __name__ == "__main__":
    main()