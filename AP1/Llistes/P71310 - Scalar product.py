def scalar_product(u: list[float], v: list[float]) -> float:
    '''Donats dos vectors u i v, retorna el producte escalar d'aquests dos.
    PrecondiciÃ³ u i v han de tenir la mateixa longitud'''

    resultat = 0.0
    for i in range (0, len(v)):
        resultat += (u[i] * v[i])
    
    return resultat