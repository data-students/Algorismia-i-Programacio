def insertion_sort (v:list[float]) -> None:
    '''Ordena la llista L en orde creixent.'''
    n = len(v)
    for i in range (1, n):
        insercio_ordenada(v, i)

def insercio_ordenada (v: list[float], i:int) -> None:
    x = v[i]
    j = i - 1
    while j >= 0 and v[j] > x:
        v[j + 1] = v[j]
        j -= 1
    v[j + 1] = x

