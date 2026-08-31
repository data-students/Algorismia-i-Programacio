import yogi

def main() -> None:
    n = yogi.scan(int)
    while n is not None:
        resultat = 1.0
        if n >= 2:
            i = 2
            mult = 1.0
            while i <= n:
                if i % 2 == 0:
                    resultat *= 2.0
                else:
                    resultat *= mult
                    mult += 0.5
                i += 1
        print (int(resultat))
        n = yogi.scan(int)

if __name__ == "__main__":
    main()