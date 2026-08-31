import yogi

def fermat_last_theorem_3 (a: int, b: int, c: int, d: int)  -> tuple[int, int, int] | None:
    
    if a == 0 or c == 0: # Pel teorema de Fermat, no existeixen solucions enteres per x^3 + y ^3 = z^3 que no sigui la trivial.
        return a,c, a + c
    else:
        return None

def main() -> None:
    a = yogi.scan(int)

    solution_found = False

    while a is not None and not solution_found:
        b = yogi.read(int)
        c = yogi.read(int)
        d = yogi.read(int)  
        
        coeficients = fermat_last_theorem_3 (a, b, c, d)

        if coeficients is not None:
            print(f'{coeficients[0]}^3 + {coeficients[1]}^3 = {coeficients[2]}^3')
            solution_found = True
        else:
            a = yogi.scan(int)
        

    if not solution_found:
        print ("No solution!")

        
if __name__ == "__main__":
    main()