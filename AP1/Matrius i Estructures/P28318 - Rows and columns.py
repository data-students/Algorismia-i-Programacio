import yogi
from typing import TypeAlias

Vector: TypeAlias = list[int]
Matriu: TypeAlias = list[Vector]

def llegir_matriu (n: int, m: int) -> Matriu:
    matriu: Matriu = []
    for _ in range(n):
        fila: Vector = []
        for _ in range(m):
            numero = yogi.read(int)
            fila.append(numero)
        matriu.append(fila)
    return matriu

def escriure_fila (M: Matriu, n: int) -> None:
    for i in range (len(M[n - 1])):
        print ("", end=" ")
        print (M[n - 1][i], end="")

def escriure_columna (M: Matriu, m: int) -> None:
    for i in range (len(M)):
        print ("", end=" ")
        print (M[i][m - 1], end="")

def escriure_element (M: Matriu, n: int, m: int) -> None:
    print ("", end=" ")
    print (M[n - 1][m - 1], end="")

def main() -> None:
    n = yogi.read(int)
    m = yogi.read(int)
    matriu = llegir_matriu(n, m)

    pregunta = yogi.scan(str)
    while pregunta is not None:
        if pregunta == "row":
            fila = yogi.read(int)
            print (f'row {fila}:', end="")
            escriure_fila(matriu, fila)
            print ("")
        elif pregunta == "column":
            columna = yogi.read(int)
            print(f'column {columna}:', end="")
            escriure_columna(matriu, columna)
            print ("")
        elif pregunta == "element":
            fila = yogi.read(int)
            columna = yogi.read(int)
            print (f'element {fila} {columna}:', end="")
            escriure_element(matriu, fila, columna)
            print ("")
        else:
            assert "Pregunta inválida"

        pregunta = yogi.scan(str)

if __name__ == "__main__":
    main ()