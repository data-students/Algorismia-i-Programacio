import sys

def evaluate(expression: str) -> int:
    pila = list[int]() # pila: list[int] = []
    for element in expression.split():
        if element.isdigit():
            pila.append(int(element))
        else:
            assert len(pila) >= 2, "Falten operands."
            if element == '+':
                pila.append(pila.pop() + pila.pop())
            elif element == '-':
                pila.append(-pila.pop() + pila.pop())
            elif element == '*':
                pila.append(pila.pop() * pila.pop())
            else:
                assert False, "operador il·legal."
    assert len(pila) == 1, "Falten operadors."
    return pila[-1]

def main() -> None:
    for line in sys.stdin:
        print(evaluate(line))

if __name__ == "__main__": # pragma: no cover
    main()

# python3 P52023.py < sample.inp | cmp - sample.cor