def fusio(l1: list[float], l2: list[float]) -> list[float]:

    l: list[float] = []

    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1

    l.extend(l1[i:])
    l.extend(l2[j:])

    return l

def ordenacio_per_fusio(v: list[float]) -> list[float]:

    llargada = len(v)
    if llargada <= 1:
        return v
    else:
        v1 = ordenacio_per_fusio(v[(llargada // 2):])
        v2 = ordenacio_per_fusio(v[:(llargada // 2)])
        L = fusio (v1, v2)
        return L
    
def mergesort(v: list[float]) -> None:
    v_ord = ordenacio_per_fusio (v)
    v[:] = v_ord