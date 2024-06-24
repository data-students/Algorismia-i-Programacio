from yogi import read

def hanoi(n: int, ori: str, aux: str, dst: str) -> None:
    ''' Mou n discos del piu ori al piu dst passant pel piu aux '''
    if n > 0:
        hanoi(n-1, ori, dst, aux)
        print(ori, "=>", dst)
        hanoi(n-1, aux, ori, dst)

def main():
    hanoi(read(int), "A", "B",  "C")

if __name__ == "__main__":
    main()
