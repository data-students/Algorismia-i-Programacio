import yogi

def llista_paraules_valides (lletres: str, paraules: list[str]) -> list[str]:

    paraules_valides: list[str] = []
    for paraula in paraules:
        es_valida = True
        for lletra in paraula:
            if not (lletra in lletres) or len(paraula) < 3:
                es_valida = False
        if not (lletres[0] in paraula):
            es_valida = False

        if es_valida:
            paraules_valides.append(paraula)
    
    return paraules_valides

def es_tuti (lletres: str, paraula: str) -> bool:
    for lletra in lletres:
        if not (lletra in paraula):
            return False
    return True

def comptar_punts (lletres: str, paraules: list[str]) -> int:
    punts_totals = 0

    for paraula in paraules:
        llargada = len(paraula)
        if llargada == 3:
            punts_totals += 1
        elif llargada == 4:
            punts_totals += 2
        elif llargada >= 7 and es_tuti(lletres, paraula):
            punts_totals += 10 + llargada
        else:
            punts_totals += llargada

    return punts_totals

def llegir_llista () -> list[str]:
    llista: list[str] = []
    entrada = yogi.scan(str)
    while entrada is not None:
        llista.append(entrada)
        entrada = yogi.scan(str)
    return llista

def main () -> None:
    lletres = yogi.read(str)
    paraules = llegir_llista()
    paraules_valides = llista_paraules_valides(lletres, paraules)
    
    paraules_valides.sort()

    punts_totals = comptar_punts(lletres, paraules_valides)

    for paraula in paraules_valides:
        print (paraula)

    print ("-----")
    print (punts_totals)

if __name__ == "__main__":
    main()