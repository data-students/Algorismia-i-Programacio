from yogi import read


def max_partitions_rec(words: list[str], p: int, sol: list[list[bool]], idx: int, used: list[bool]):
    n = len(words)

    if idx == n:
        for part in range(p):
            print(f"subset {part + 1}: ", end = "")
            print("{" + ",".join(str(words[i]) for i in range(n) if sol[part][i]) +  "}")
        print()
    else:
        for i in range(idx, n):
            if not used[i]:
                for part in range(p):
                    used[i] = True
                    sol[part][i] = True

                    max_partitions_rec(words, p, sol, idx + 1, used)
                    
                    used[i] = False
                    sol[part][i] = False




def max_partitions(words: list[str], p: int) -> None:
    n = len(words)
    sol = [[False for _ in range(n)] for _ in range(p)] # cada fila = partició, cada columna = paraula
    used = [False] * n
    max_partitions_rec(words, p, sol, 0, used)

def main() -> None:
    n = read(int)
    words = [read(str) for _ in range(n)]
    p = read(int)
    max_partitions(words, p)
    

if __name__ == "__main__":
    main()

