import math
from yogi import read

def area_rectangle (base: float, alcada: float) -> float:
    area = base * alcada
    return area

def area_cercle (radi: float) -> float:
    area = math.pi * radi**2
    return area

def main () -> None:
    n = read (int) # El nombre de entrades que tindrà el nosrte programa
    for _ in range (n):
        figura = read (str)

        if figura == "circle":
            radi = read (float)
            print (f"{area_cercle(radi):.06f}")
            
        elif figura == "rectangle":
            base = read (float)
            alcada = read (float)
            print (f"{area_rectangle(base, alcada):.06f}")

if __name__ == "__main__":
    main ()