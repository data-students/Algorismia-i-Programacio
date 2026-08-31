import sys
from typing import TypeAlias

Cola: TypeAlias = dict[str, list[str]] # Cada llave representa un rango, los valores son las personas

def enter(supermercado: list[Cola], nom: str, rang: str, n: int) -> None:
    """Donat un supermercat, afegeix un nom al final de la cua del seu respectiu rang"""
    if 0<= n < len(supermercado):
        supermercado[n][rang].append(nom)
    
def out(supermercado: list[Cola], n: int) -> str | None:
    """Dado un supermercado, si la cola está entre 1 y n, y la cola no está vacía,
    el cliente de más graduación sale de la cola. En caso de empate, sale el que haya 
    llegado antes a la cola. En caso contrario, el suceso se ignora."""
    
    if not (0 <= n < len(supermercado)):
        return None
    
    if supermercado[n]["coronel"]:
        return supermercado[n]["coronel"].pop(0)
    if supermercado[n]["capitan"]:
        return supermercado[n]["capitan"].pop(0)
    if supermercado[n]["sargento"]:
        return supermercado[n]["sargento"].pop(0)
    if supermercado[n]["soldado"]:
        return supermercado[n]["soldado"].pop(0)

    return None 

def create(n: int) -> list[Cola]:
    supermercado: list[Cola] = []
    # Per cada cua, llegir les persones que hi han i el seu rang
    for _ in range(n):
        line = sys.stdin.readline().split()
        cola: Cola = {"coronel": [], "capitan": [], "sargento": [], "soldado": []}

        # Per cada persona classificar-la segons el seu rang
        for i in range(0, len(line), 2):
            cola[line[i+1]].append(line[i])
        supermercado.append(cola)

    return supermercado

def main() -> None:
    n = int(sys.stdin.readline())
    supermercado = create(n)

    print("SALIDAS\n--------")

    for line in sys.stdin:
        # Assegurarse que la linea no está vacía
        if line == "\n":
            continue

        line = line.split()
        if line[0] == "SALE":
            sale = out(supermercado, int(line[1]) - 1)
            if sale:
                print(sale)

        elif line[0] == "ENTRA":
            enter(supermercado, line[1], line[2], int(line[3]) - 1)
    
    print("\nCONTENIDO FINAL\n-----------------")
    for i in range(n):
        print(f"cua {i + 1}:", end="")
        while True:
            sale = out(supermercado, i)
            if sale:
                print(f" {sale}", end="")
            else:
                break

        print()

if __name__ == "__main__":
    main()
