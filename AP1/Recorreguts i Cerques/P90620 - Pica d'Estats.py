import yogi

# Es possible que un pic es consideri 18 29 29 20 !!!
def es_un_pic (anterior: int, pic: int, posterior: int) -> bool:
    return anterior < pic > posterior

def main () -> None:
    pica_estats = 3143
    # Llegim les 3 primeres entrades i fem la "finestra"
    entrada1 = yogi.read (int)
    entrada2 = yogi.read (int)
    entrada3 = yogi.scan (int)

    es_major_pica_estats = False

    while (entrada3 is not None) and (entrada3 != 0) and (not es_major_pica_estats):
        if es_un_pic (entrada1, entrada2, entrada3) and entrada2 > pica_estats:
            es_major_pica_estats = True
        
        entrada1, entrada2, entrada3 = entrada2, entrada3, yogi.scan(int)

        if entrada3 == 0:
            entrada3 = None


    if es_major_pica_estats:
        print ("YES")
    else:
        print ("NO")
        
if __name__ == "__main__":
    main()