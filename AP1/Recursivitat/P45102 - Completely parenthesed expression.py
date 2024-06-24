from yogi import read

def op():
    c = read(str)

    if c == "(":
        a = op()
        simbol = read(str)
        b = op()
        closing = read(str)

        if simbol == "+":
            return a + b
        elif simbol == "*":
            return a * b
        elif simbol == "-":
            return a - b

    else:
        return int(c)

print(op())
