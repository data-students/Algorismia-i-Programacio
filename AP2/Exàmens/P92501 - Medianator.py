from yogi import tokens, read
import heapq as pq

class Medianator:
    """..."""
    lowpq: list[int]
    med: int | None
    highpq: list[int]

    def __init__(self) -> None:
        self.lowpq: list[int] = []
        self.med: int | None = None
        self.highpq: list[int] = []

    def add(self, element: int) -> None:
        """..."""
        n = len(self.lowpq) + len(self.highpq) + 1
        if self.med is None:
            self.med = element
        else:
            if element < self.med:
                pq.heappush(self.lowpq, -element)
                if n % 2 == 1:
                    pq.heappush(self.highpq, self.med)
                    self.med = -pq.heappop(self.lowpq)
            else:
                pq.heappush(self.highpq, element)
                if n % 2 == 0:
                    pq.heappush(self.lowpq, -self.med)
                    self.med = pq.heappop(self.highpq)

    def median(self) -> int:
        """..."""
        assert self.med is not None, "La llista està buida!"
        return self.med


def main() -> None:
    s = Medianator()
    for action in tokens(str):
        if action == "add":
            s.add(read(int))
        elif action == "median":
            print(s.median())
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()
