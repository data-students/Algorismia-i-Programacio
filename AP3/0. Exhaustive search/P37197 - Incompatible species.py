from yogi import read

def write_row(species: list[str], sp_to_idx: dict[str, int], incomp: list[list[bool]]) -> None:
    """..."""
    n = len(species)
    used = [False] * n
    sol: list[str] = []

    def write_row_rec(used: list[bool], idx: int, sol: list[str]) -> None:
        if idx == n:
            print("".join(sol))
        else:
            for i, sp in enumerate(species):
                sp_ant = sol[-1] if sol else None
                if not used[i] and (sp_ant is None or not incomp[sp_to_idx[sp]][sp_to_idx[sp_ant]]):
                    sol.append(sp)
                    used[i] = True
                    write_row_rec(used, idx + 1, sol)
                    sol.pop()
                    used[i] = False
    
    write_row_rec(used, 0, sol)


def main() -> None:

    # Llegir espècies
    n = read(int)
    species = [read(str) for _ in range(n)]
    sp_to_idx = {sp: idx for idx, sp in enumerate(species)}

    # Construir taula d'imcompatibilitats
    m = read(int)
    incopm = [[False] * n for _ in range(n)]
    for _ in range(m):
        x1, x2 = read(str)
        incopm[sp_to_idx[x1]][sp_to_idx[x2]] = True
        incopm[sp_to_idx[x2]][sp_to_idx[x1]] = True

    write_row(species, sp_to_idx, incopm)

if __name__ == "__main__":
    main()