import yogi

def main() -> None:
    entrada1 = yogi.read(str)
    entrada2 = yogi.read(str)
    
    while entrada2 != "END":
        if entrada2 >= entrada1:
            print (entrada1)
            entrada1, entrada2 = entrada2, yogi.read(str)
        else:
            print (entrada2)
            entrada2 = yogi.read(str)
            
    print (entrada1)

if __name__ == "__main__":
    main()
