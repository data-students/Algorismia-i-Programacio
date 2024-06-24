from yogi import read

def op():
    s = read(str)

    if s == "+":
        return op() + op()
    elif s == "-":
        return -op()
    elif s == "m":
        a, b, c = op(), op(), op()
        return max(a, b, c)
    else:
        return int(s)

def main():
    print(op())

if __name__ == "__main__":
    main()
