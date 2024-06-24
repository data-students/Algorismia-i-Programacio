from yogi import read

def pattern(n: int) -> None:
    if n == 1:
        print("*")
    else:
        pattern(n-1)
        print("*" * n)
        pattern(n-1)


def main():
    n = read(int)
    pattern(n)


if __name__ == "__main__":
    main()
