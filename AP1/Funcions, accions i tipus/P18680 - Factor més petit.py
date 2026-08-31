
def factor_mes_petit(n: int):
    i = 1
    factor = n
    es_compost = False

    while i*i <= n:
        if n % i == 0 and i != 1:
            div1 = i
            div2 = n // i
            es_compost = True
            if div1 < factor:
                factor = div1
            elif div2 < factor:
                factor = div2
        i += 1
    if not es_compost:
        return None
    
    return factor