def escriure_factors_primers (n: int) -> None:
    i = 2
    es_el_primer_numero = True
    while n > 1:
        if n % i == 0:
            n = n // i
            if n % i != 0:
                if not es_el_primer_numero:
                    print (",", end="")
                print (i, end="")
                es_el_primer_numero = False
        else:
            i += 1
    print ("")