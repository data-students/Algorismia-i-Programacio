from yogi import read, tokens
UNDEF = "."
VALID_SYMBOLS = {
    "A": ("T", UNDEF),
    "T": ("A", UNDEF),
    "C": ("G", UNDEF),
    "G": ("C", UNDEF)
    }

def print_cad(cad: list[list[str]], i: int, j: int) -> None:
    
    n = len(cad[0])
    if j == n:
        print_cad(cad, i + 1, 0)
    
    elif i == 2:
        print("\n".join(str("".join(str(x) for x in cad[i])) for i in range(2)))
        print(  )
        return
    
    elif cad[i][j] != ".":
        if cad[i - 1][j] in VALID_SYMBOLS[cad[i][j]]:
            print_cad(cad, i, j + 1)
        else:
            return
    else:
        for sym in ["A", "C", "G", "T"]:
            if cad[i - 1][j] in VALID_SYMBOLS[sym]:
                cad[i][j] = sym
                print_cad(cad, i, j + 1)
                cad[i][j] = "."

def main() -> None:
    for n in tokens(int):
        cad = [list(read(str)) for _ in range(2)]

        print_cad(cad, 0, 0)
        print('-'*10)

if __name__ == "__main__":
    main()