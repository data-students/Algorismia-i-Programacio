from yogi import read

def op () -> int:

    c = read(str)

    if c == "+":
        return op() + op()
    elif c == "-":
        return op() - op()
    elif c == "*":
        return op() * op()
    else:
        return int(c)


print(op())
