from turtle import up, down, goto, left, forward, speed, done
from yogi import read

def quadrat(d: float, x: float, y: float) -> None:
    up()
    goto(x,y)
    down()
    for i in range(4):
        forward(d)
        left(90)

def amenaça_fractal(n: int, d: float, x: float, y: float) -> None:
    if n == 1:
        quadrat(d, x, y)
    else:
        quadrat(d, x, y)
        amenaça_fractal(n-1, d/2, x + d, y + d) # top right
        amenaça_fractal(n-1, d/2, x - d/2, y + d) # top left
        amenaça_fractal(n-1, d/2, x - d/2, y - d/2) # bottom left


def main():
    amenaça_fractal(read(int), read(int), 0, 0)
    #speed(0)
    done()

if __name__ == "__main__":
    main()
