from yogi import read, tokens

UNDEF = -1

def cost(car: str, c: list[int]) -> int:

    assert len(car) == 1
    return c[ord(car) -  ord('a')]

def distance(A: str, B: str, c: list[int]) -> int:
    # We add one extra column and one extra row in order to cache result for i = -1, j = -1
    # Those will be stored in the last position and will access them with index -1
    C = [[UNDEF for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    
    # Omplo la matriu
    C[-1][-1] = 0

    # Fila addicional (i = -1)
    for j in range(len(B)):
        C[-1][j] = C[-1][j - 1] + cost(B[j], c)

    # Columna addicional (j = -1)
    for i in range(len(A)):
        C[i][-1] = C[i - 1][-1] + cost(A[i], c)

    # Resta de la matriu
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                C[i][j] = C[i - 1][j - 1]
            else:
                C[i][j] = min(
            C[i][j - 1] +  cost(B[j], c),
            C[i - 1][j] + cost(A[i], c)
        )

    return C[len(A) - 1][ len(B) - 1]

def main() -> None:
    for n in tokens(int):
        c = [read(int) for _ in range(n)]
        A = read(str)
        B = read(str)
        print(distance(A, B, c))

if __name__ == "__main__":
    main()