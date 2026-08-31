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

def seguent_iteracio(entrada: list[str], cua: list[int], n: int, suma: float) -> tuple[int, float]:
    '''Retorna el nombre d'elemetns i la suma total de la seguent instrucció de l'entrada.
    Rep com a paràmetres una cua de prioritat, la instrucció demanada, la llargrària de la cua de prioritat i al seva suma total.'''

    op = entrada[0]

    if op == "delete":
        if cua:
            return n - 1, suma - cua.pop(0)
        else:
            return 0, 0

    elif op == "number":
        num = int(entrada[1])
        if not cua or num >= cua[-1]:
            cua.append(num)
        else:
            inserta(cua, num)

        return n + 1, suma + float(num)
    
    else:
        assert False, "Entrada errònia!"


def main() -> None:

    n = 0 # nombre d'elements en la cua
    suma = 0.0 # suma total del nombre d'elements de la cua
    cua = list[int]()

    for line in sys.stdin:
        entrada = line.split()
        n, suma = seguent_iteracio(entrada, cua, n, suma)
        if cua:
            print(f'minimum: {cua[0]}, maximum: {cua[-1]}, average: {suma / n:.04f}')
        else:
            print("no elements")

if __name__ == "__main__":
    main()