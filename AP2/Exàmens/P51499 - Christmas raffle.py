import heapq
from dataclasses import dataclass
from yogi import read, tokens

class ChristmassRiffle:
    freqs: dict[int, int] # key: numbers, value: freqs
    most_freq: tuple[int, int] # most freq number, freq
    term: dict[str, int] # key: treminations, value: freqs
    most_term: tuple[str, int] # most freq term, freq


    def __init__(self) -> None:
        self.freqs = {}
        self.most_freq = (-1, -1)
        self.term = {}
        self.most_term = ("-1", -1)

    def add(self, n: int) -> None:

        if n not in self.freqs:
            self.freqs[n] = 1
        else:
            self.freqs[n] += 1
        if self.freqs[n] > self.most_freq[1] or (self.freqs[n] == self.most_freq[1] and n < self.most_freq[0]):
            self.most_freq = (n, self.freqs[n])
                

        n_str = "0" + str(n) if len(str(n)) == 1 else str(n)
        term = n_str[-2:]
        if term not in self.term:
            self.term[term] = 1
        else:
            self.term[term] += 1
        
        if self.term[term] > self.most_term[1] or (self.term[term] == self.most_term[1] and term < self.most_term[0]):
            self.most_term = (term, self.term[term])

    def info(self) -> tuple[int, int, str, int]:
        return self.most_freq + self.most_term

    def sorted_freqs(self) -> list[tuple[int, int]]:
        return sorted(self.freqs.items())

def main() -> None:
    for n in tokens(int):
        cr = ChristmassRiffle()
        while n != -1:
            cr.add(n)
            print(*cr.info())
            n = read(int)
        print()
        for number, count in cr.sorted_freqs():
            print(f"{number} {count}")
        
        print("-" * 10)

if __name__ == "__main__":
    main()