import yogi
from dataclasses import dataclass
from functools import cmp_to_key

@dataclass
class Rectangle:
    amplada: int
    alçada: int

def compara_rectangles (rect1: Rectangle, rect2: Rectangle) -> int:
    area1 = rect1.amplada * rect1.alçada
    area2 = rect2.amplada * rect2.alçada
    if area1 == area2:
        if rect1.amplada + rect1.alçada == rect2.amplada + rect2.alçada:
            return rect1.amplada - rect2.amplada # El mes petit va abans
        else:
            return (rect2.amplada + rect2.alçada) - (rect1.amplada + rect1.alçada) # El mes gran va abans
    else:
        return area1 - area2 # El mes petit va abans
    
def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        llista_rectangles: list[Rectangle] = []
        for _ in range (entrada):
            amplada = yogi.read(int)
            alçada = yogi.read(int)
            llista_rectangles.append(Rectangle(amplada, alçada))

        llista_rectangles.sort(key=cmp_to_key(compara_rectangles))

        for rectangle in llista_rectangles:
            print(rectangle.amplada, rectangle.alçada, sep=" ")
        print("-"*10)
        entrada = yogi.scan(int)
    
if __name__ == "__main__":
    main()