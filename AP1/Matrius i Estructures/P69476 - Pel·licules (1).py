from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    year: int
    stars: int
    earnings: float

def compare_movies(m1: Movie, m2: Movie) -> int:
    # Comparar per estrelles
    if m1.stars > m2.stars:
        return -1
    elif m1.stars < m2.stars:
        return 1
    
    # Si les estrelles son iguals, comparar ingressos
    if m1.earnings > m2.earnings:
        return -1
    elif m1.earnings < m2.earnings:
        return 1
    
    # Si els ingressos son iguals, comparar anys
    if m1.year > m2.year:
        return -1
    elif m1.year < m2.year:
        return 1

    # Si tot és igual
    return 0

