def es_primer(n: int) -> bool:
    if n <= 1:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True
