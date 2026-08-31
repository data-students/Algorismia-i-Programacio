import yogi

def comptar_campanades2(h: int, m: int, t: int) -> int:
    '''Retorna el nombre de campanades que sonaran despres de "t" temps desde l'instant(h:m).'''
    '''15º por hora, 6º por minuto'''
    # Per eficiència, sumar directament les que fa en un dia i només calcular el mòdul de l'ultim dia.
    campanades_totals = 22 * (t // 1440)
    t = t % 1440
    # Calcular la posició de les agulles a t (mesurat en graus sexagecimals)
    m_graus_ini = 360 // 60 * m
    h_graus_ini = 360 // 12 * (h % 12) + m_graus_ini / (360 / 30)

    for _ in range(t):
        # Calcular el minut t+1
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
        
        # Calcular la posició de les agulles en t+1 i sumar una campanada si s'han creuat
        m_graus_fin = 360 // 60 * m
        h_graus_fin = 360 // 12 * (h % 12) + m_graus_fin / (360 / 30)
        if m_graus_ini <= h_graus_ini and m_graus_fin > h_graus_fin:
            campanades_totals += 1

        h_graus_ini, m_graus_ini = h_graus_fin, m_graus_fin

    return campanades_totals
    

def main() -> None:
    h = yogi.scan(int)
    while h is not None:
        m = yogi.read(int)
        t = yogi.read(int)
        
        campanades_totals = comptar_campanades2(h, m, t)
        print (campanades_totals)

        h = yogi.scan(int)
if __name__ == "__main__":
    main()