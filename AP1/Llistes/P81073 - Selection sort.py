
def posicio_minim(v: list[float], i: int) -> int:
    """Retorna la posició de l'element més petit de L[i:] amb 0 ≤ i < len(L)."""

    n = len(v)
    p = i
    for j in range(i + 1, n):
        if v[j] < v[p]:
            p = j
    return p

def selsort(v: list[float]) -> None:
    """Ordena la llista L en ordre creixent."""

    n = len(v)
    for i in range(n - 1):
        p = posicio_minim(v, i)
        v[i], v[p] = v[p], v[i]