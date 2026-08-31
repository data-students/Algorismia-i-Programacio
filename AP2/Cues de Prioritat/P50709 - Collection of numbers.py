import sys

def inserta(l: list[int], n: int) -> None:
    '''Donada una llista l i un element n, s'inserta n en la llista, de manera que quedi ordenada.
    Perc: la llista ha de estar oredenada.'''
    izq, der = 0, len(l)
        
    while izq < der:
        mid = (izq + der) // 2
        if l[mid] < n:
            izq = mid + 1
        else:
            der = mid

    l.insert(izq, n)

def main() -> None:

    cua = list[int]()
    for line in sys.stdin:
        line = line.split()
        i = 0
        while i < len(line):
            if line[i] == "S": # Stores a copy of the given number x
                i += 1
                x = int(line[i])
                inserta(cua, x)
                
            elif line[i] == "A": # Asks for the greatest number
                if len(cua) > 0:
                    print(cua[-1])
                else:
                    print("error!")

            elif line[i] == "R": # Removes the greatest number (one of them if it is repeated).
                if len(cua) > 0:
                    cua.pop()
                else:
                    print("error!")

            elif line[i] == "I": # Increases the greatest number (one of them, if it is repered) in x units.
                i += 1
                if len(cua) > 0:
                    x = int(line[i])
                    cua[-1] += x
                else:
                    print("error!")

            elif line[i] == "D": # Decreases the greatest number (one of them, if it is repered) in x units.
                i += 1
                if len(cua) > 0:
                    x = int(line[i])
                    n = cua.pop() - x
                    inserta(cua, n)
                    
                else:
                    print("error!")
            else:
                assert False, "error!"
            
            i += 1



if __name__ == "__main__":
    main()