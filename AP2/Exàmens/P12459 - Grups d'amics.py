from yogi import read, tokens

class DisjointSet:
    def __init__(self) -> None:
        self.representant: dict[str, str] = {} # key: usuari, value: pare
        self.size: dict[str, int] = {} # key: usuari, value: tamany del grup
    
    def makeset(self, x: str) -> None:
        if x not in self.representant:
            self.representant[x] = x
            self.size[x] = 1

    def find(self, x: str) -> str:
        """Troba i retorna al pare arrel de x."""

        while x != self.representant[x]:
            x = self.representant[x]
        return x
    
    def union(self, x: str, y:str) -> None:
        """Fa la unió de les components de x i les de y.
        Manté el conjunt relativament balancejat."""

        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return None
        
        # Assegurar-se de que x té el rang més alt
        if self.size[ry] > self.size[rx]:
            rx, ry = ry, rx

        self.representant[ry] = rx
        self.size[rx] += self.size[ry]
        
    def get_size(self, x: str) -> int | None:
        if x not in self.representant:
            return None
        rx = self.find(x)
        return self.size[rx]


def main() -> None:
    set_persones = DisjointSet()
    for instr in tokens(str):
        if instr == "F":
            n = read(int)
            amics = [read(str) for _ in range(n)]
            for s in amics:
                set_persones.makeset(s)
            representant = amics[0]
            for s in amics[1:]:
                set_persones.union(representant, s)

        elif instr == "Q":
            s = read(str)
            size = set_persones.get_size(s)
            print(f"{s}: ", end="")
            print(size if size else "error")

        else:
            raise KeyError

if __name__ == "__main__":
    main()
