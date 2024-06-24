from yogi import read
from turtle import up, down, goto, circle, speed, done

def cercle(x: float, y: float, radi: float) -> None:
    '''Dibuixa un cercle amb centre (x,y) i el radi donat'''
    up()
    goto(x, y - radi)
    down()
    circle(radi)
    up()


def cercles_koch(n: int, radi:float, x: float, y: float) -> None:
    if n == 1:
        cercle(x, y, radi)
    else:
        cercle(x, y, radi)
        cercles_koch(n-1, radi/2, x + 1.5*radi, y)
        cercles_koch(n-1, radi/2, x - 1.5*radi, y)
        cercles_koch(n-1, radi/2, x, y + 1.5*radi)
        cercles_koch(n-1, radi/2, x, y - 1.5*radi)


def main():
    n = read(int)
    d = read(int)
    cercles_koch(n, d, 0, 0)
    speed(0)
    done()

if __name__ == "__main__":
    main()
