import yogi
import math

def number_solutions_fermat_last_theorem (a: int, b: int, c: int, d: int) -> int:

    number_solutions = 0

    for x in range (a, b+1):
        for y in range (c, d+1):
            resultat = x * x + y * y
            z = int(math.sqrt(resultat))
            if resultat == z * z:
                number_solutions += 1

    return number_solutions

def main() -> None:
    a = yogi.scan(int)

    while a is not None:
        b = yogi.read(int)
        c = yogi.read(int)
        d = yogi.read(int)

        print (number_solutions_fermat_last_theorem (a, b, c, d))

        a = yogi.scan(int)
        
if __name__ == "__main__":
    main()