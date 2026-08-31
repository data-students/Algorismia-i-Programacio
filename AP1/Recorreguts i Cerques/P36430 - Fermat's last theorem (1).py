import yogi

def fermat_last_theorem (a: int, b: int, c: int, d: int)  -> tuple[int, int, int] | None:
    
    for x in range (a, b+1):
        for y in range (c, d+1):
            resultat = x**2 + y **2
            z = int(resultat ** 0.5)
            if resultat == z**2:
                return x,y,z

    return None

def main() -> None:
    a = yogi.read(int)
    b = yogi.read(int)
    c = yogi.read(int)
    d = yogi.read(int)
    
    coeficients = fermat_last_theorem (a, b, c, d)

    if coeficients is None:
        print ("No solution!")
    else:
        print(f'{coeficients[0]}^2 + {coeficients[1]}^2 = {coeficients[2]}^2')
        
if __name__ == "__main__":
    main()