import math
from yogi import read

def main() -> None:
    entrada = read (float)
    entrada_radians = entrada / 360 * 2 * math.pi

    sinus = math.sin(entrada_radians)
    cosinus = math.cos(entrada_radians)
    print (f"{sinus:.06f} {cosinus:.06f}")

if __name__ == "__main__":
    while True:
        main()