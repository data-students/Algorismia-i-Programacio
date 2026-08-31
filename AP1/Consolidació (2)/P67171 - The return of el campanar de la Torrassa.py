import yogi

def comptar_campanades3(h: int, m: int) -> tuple[int, int]:
    '''Retorna el nombre de minuts que algu que es lleva a les (h:m) ha d'esperar per saber exactament a quina hora és,
    i el nombre de campanades que sent mentrestant.'''
    campanades = 0
    m_espera = 0
    es_superllest = False
    while True:
        # Calcular l'hora en el temps t+1
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0

        # Comptar campanades en el temps t+1
        if m == 1:
            if (h % 12) == 0:
                campanades += 12
            else:
                campanades += h % 12
            
            # Las excepciones -_-
            if not (campanades <= 4 and h % 12 == 1):
                return m_espera, campanades
            if campanades == 4:
                es_superllest = True
        
        if m != 1 and ((m - 1) % 15) == 0:
            campanades += 1
        
        # Uoo las excepciones. ¡Qué listo que es!
        if es_superllest and m == 46:
            return m_espera, campanades
        
        m_espera += 1

# 0 30 -> 90 8
# 13 0 -> 60 6
# 0 15 -> 90 7

def main() -> None:
    h = yogi.scan(int)
    while h is not None:
        m = yogi.read(int)
        m_espera, campanades = comptar_campanades3(h, m)
        print (m_espera, campanades, sep=" ")
        h = yogi.scan(int)

if __name__ == "__main__":
    main()