import yogi

def product_of_digits (n:int) -> None:
    nStr = str(n)
    prod = 1

    for char in nStr:
        prod *= int(char)
    print (f'The product of the digits of {n} is {prod}.')
    if prod // 10 != 0:
        product_of_digits(prod)


def main() -> None:
    for entrada in yogi.tokens(int):
        product_of_digits (entrada)
        print ("----------")


if __name__ == "__main__":
    main()