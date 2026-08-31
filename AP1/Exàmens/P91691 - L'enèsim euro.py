import yogi

def on_es_gasta_n_euro(n :int) -> str | None:
    '''Donat un número n, l funció llegeix la llista de productes comprats i retorna on s'ha gasta l'n-èssim euro.'''
    
    total_gastat = 0
    producte = yogi.scan(str)
    producte_n: str | None = None

    while producte != "---":
        preu = yogi.read(int)
        total_gastat += preu

        if producte_n is None and (n - total_gastat) <= 0:
            producte_n = producte

        producte = yogi.read(str)
    
    return producte_n


def main() -> None:
    nombre_factures = yogi.read(int)
    n = yogi.read(int)
    for _ in range (nombre_factures):
        factura = yogi.read(str)
        producte_n = on_es_gasta_n_euro (n)
        if producte_n is None:
            print (f"En la factura {factura} no s'ha gastat l'euro {n}.")
        else:
            print (f"En la factura {factura} l'euro {n} s'ha gastat en {producte_n}.")

if __name__ == "__main__":
    main()