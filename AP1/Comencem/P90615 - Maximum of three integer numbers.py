import yogi
def main():
    p1 = yogi.read(int)
    p2 = yogi.read(int)
    p3 = yogi.read(int)
    print(max(p3, p2, p1))

if __name__ == "__main__":
    main()