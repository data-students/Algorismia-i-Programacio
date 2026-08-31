def intersection(v1: list[float], v2: list[float]) -> list[float]:

    v: list [float] = []

    i,j = 0,0
    while i < len(v1) and j < len(v2):
        v1_num_actual = v1[i]
        v2_num_actual = v2[j]

        if v1_num_actual < v2_num_actual:
            i += 1
        elif v1_num_actual > v2_num_actual:
            j += 1
        else:
            if v == [] or v1_num_actual != v[len(v) - 1]:
                v.append(v1_num_actual)
                
            i += 1
            j += 1
    
    return v