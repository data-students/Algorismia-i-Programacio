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

def semiprimalitat(n: int):
    i = 2
    while i * i <= n:  # Busquem divisors fins a l'arrel quadrada de n
        if n % i == 0:  # Si i és divisor de n
            div1 = i
            div2 = n // i
            # Comprovem si tots dos divisors són primers
            if es_primer(div1) and es_primer(div2):
                return (div1, div2) if div1 <= div2 else (div2, div1)
        i += 1
    return None  # Si no trobem cap combinació de primers