import yogi
def main():
    p1 = yogi.read(int)
    p2 = yogi.read(int)

    print(max(p1, p2))

if __name__ == "__main__":
    main()