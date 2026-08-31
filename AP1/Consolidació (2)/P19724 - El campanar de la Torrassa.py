import yogi

def comptar_campanades(h: int, m: int, t: int) -> int:
    '''Donat un temps inicial h:m, compta quantes campanades es tocaràn després de t minuts.'''
    campanades_totals = 0
    campanades_agudes = 0 # Per quart d'hora
    campanades_greus = 0 # Per hora

    # Per estalviar temps, per cada dia (t= 1440 min), les campanades toquen 484 vegades.
    if t >= 1440:
        campanades_totals += 484 * (t // 1440)
        t = t % 1440

    for _ in range(t):
        # Actualitzar hora al següent minut
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0

        # Per cada hora que pasa, comptem les campanades
        if m == 1:
            campanades_agudes += 4
            if h == 0:
                campanades_greus += 12
            elif h == 12:
                campanades_greus += 100
            else:
                campanades_greus += h % 12

        # Per cada quart d'hora, comptem les campanades
        if (m - 1) % 15 == 0:
            campanades_agudes += m // 15
    campanades_totals += campanades_greus + campanades_agudes
    return campanades_totals

def main() -> None:
    h = yogi.scan(int)
    while h is not None:
        m = yogi.read(int)
        t = yogi.read(int)

        campanades_totals = comptar_campanades(h, m, t)
        print (campanades_totals)

        h = yogi.scan(int)

if __name__ == "__main__":
    main()