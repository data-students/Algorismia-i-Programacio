from yogi import read
from turtle import forward, backward, left, right, done, speed


def arbre(n: int, d: float, a: float):
    if n == 1:
        forward(d)
    else:
        arbre(1, d, a)
        left(a)
        arbre(n-1, d * 3/4, a)
        backward(d * 3/4)
        right(2*a)
        arbre(n-1, d * 3/4, a)
        backward(d * 3/4)
        left(a)


def arbre_fractal(n: int, d: float, a: float) -> None:
    left(90)
    arbre(n, d, a)
    speed(0)
    done()


def main():
    n, d, a = read(int), read(float), read(float)
    arbre_fractal(n, d, a)


if __name__ == "__main__":
    main()
