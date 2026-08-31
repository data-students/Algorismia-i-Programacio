import yogi

def sum_of_digits (n: int) -> int:
    nStr = str(n)
    sum = 0
    for i in nStr:
        sum += int(i)
    
    return sum

def main() -> None:
    for entrada in yogi.tokens(int):
        print (f'The sum of the digits of {entrada} is {sum_of_digits(entrada)}.')

if __name__ == "__main__":
    main ()

