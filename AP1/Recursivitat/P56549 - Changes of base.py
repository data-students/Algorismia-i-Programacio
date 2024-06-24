from yogi import tokens

def change(n: int, b: int) -> str:
    if n > 0:
        mod = n%b
        conv = str(mod)

        if b == 16:
            if mod == 10:
                conv = "A"
            elif mod == 11:
                conv = "B"
            elif mod == 12:
                conv = "C"
            elif mod == 13:
                conv = "D"
            elif mod == 14:
                conv = "E"
            elif mod == 15:
                conv = "F"

        return conv + change(n//b, b)

    return ""


def main():
    for n in tokens(int):
        if n != 0:
            print(f"{n} = {change(n, 2)[::-1]}, {change(n, 8)[::-1]}, {change(n, 16)[::-1]}")
        else:
            print(f"{n} = 0, 0, 0")

if __name__ == "__main__":
    main()
