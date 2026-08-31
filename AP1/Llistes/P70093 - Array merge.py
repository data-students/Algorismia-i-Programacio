def merge(v1: list[float], v2: list[float]) -> list[float]:
    i, j = 0, 0
    v: list[float] = []

    while i < len(v1) and j < len(v2):
        if v1[i] < v2[j]:
            v.append(v1[i])
            i += 1
        else:
            v.append(v2[j])
            j += 1

    v.extend(v1[i:])
    v.extend(v2[j:])

    return v