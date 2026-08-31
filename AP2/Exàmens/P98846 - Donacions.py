from yogi import read, tokens
import heapq
from collections import deque

class Donations:
    nif_donators: dict[str, int]
    odd_nifs: list[str]
    largest_nif: str

    def __init__(self) -> None:
        self.nif_donators = {}
        self.odd_nifs = []
        self.largest_nif = ""
    
    def _insert(self, l: list[str], n: str) -> None:
        i = 0
        list_len = len(l)
        while i < list_len and l[i][:-1] < n[-1]:
            i += 1
        l.insert(i, n)

    def get_num_donants(self) -> int:
        """N"""
        return len(self.nif_donators)

    def add_donation(self, nif: str, ammount: int) -> None:
        """D"""
        if nif not in self.nif_donators:
            self.nif_donators[nif] = 0
            if int(nif[:-1]) % 2 == 0:
                self.odd_nifs.append(nif)
            if nif > self.largest_nif:
                self.largest_nif = nif
        
        self.nif_donators[nif] += ammount

    def get_ammount_donated(self, nif: str) -> int:
        """Q"""
        return self.nif_donators.get(nif, -1)

    def get_odd_donants(self) -> list[str]:
        """P"""
        self.odd_nifs.sort(key=lambda x: x[:-1])
        return self.odd_nifs
    
    def get_largest_nif(self) -> tuple[str, int] | None:
        """L"""
        l_nif = self.largest_nif
        return (l_nif, self.nif_donators[l_nif]) if l_nif else None
    

def main() -> None:
    donations = Donations()
    for inp in tokens(str):
        if inp == "N":
            print(f"number: {donations.get_num_donants()}")
        elif inp == "D":
            n, m = read(str), read(int)
            donations.add_donation(n, m)
        elif inp == "Q":
            n = read(str)
            print(donations.get_ammount_donated(n))
        elif inp == "P":
            print(*donations.get_odd_donants())
        elif inp == "L":
            l_nif = donations.get_largest_nif()
            if l_nif is None:
                print(l_nif)
            else:
                print(l_nif[0], l_nif[1])
        else:
            raise KeyError
        
if __name__ == "__main__":
    main()
