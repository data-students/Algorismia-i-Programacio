import yogi

def main() -> None:
    entrada = str(yogi.scan(int))

    while entrada != "0":
        for lletra in entrada:
            digit = int(lletra)
            if digit % 2 == 0:
                print(digit + 1, end="")
            else:
                print (digit, end="")

        print()
        entrada = str(yogi.scan(int))

if __name__ == "__main__":
    main()
