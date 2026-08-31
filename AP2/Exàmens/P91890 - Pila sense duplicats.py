import yogi


class NoDupsStack:

    _stack: list[int]
    _elements: set[int]

    def __init__(self):
        self._elements = set()
        self._stack = []

    def push(self, element: int) -> None:
        if element not in self._elements:
            self._elements.add(element)
            self._stack.append(element)

    def pop(self) -> None:
        if not self.empty():
            element = self._stack.pop()
            self._elements.remove(element)

    def top(self) -> int | None:
        if not self.empty():
            return self._stack[-1]
        return None

    def empty(self) -> bool:
        return not bool(self._stack)


def main() -> None:
    s = NoDupsStack()
    for command in yogi.tokens(str):
        if command == "push":
            s.push(yogi.read(int))
        elif command == "pop":
            s.pop()
        elif command == "top":
            print(s.top())
        elif command == "empty":
            print(s.empty())

if __name__ == "__main__":
    main()