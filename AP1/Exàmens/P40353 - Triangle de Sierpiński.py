from turtle import hideturtle, speed, penup, pendown, goto, forward, left, right, done
import yogi
import math

def goto_sense_dibuixar(x: float, y: float) -> None:
    '''Mou a la tortuga al punt (x, y) sense dibuixar pel camí.'''
    penup()
    goto(x, y)
    pendown()

def dibuxa_triange (mida: float, x: float, y: float) -> None:
    '''Dibuixa un triangle equlàter d'una mida definida centrat al punt (x, y). La base es troba a la part inferior del triangle.'''
    goto_sense_dibuixar(x - (mida / 2), y - (mida * (math.sqrt(3) / 4)))
    for _ in range (3):
        forward (mida)
        left(120)

def dibuxa_triange_invertit (mida: float, x: float, y: float) -> None:
    '''Dibuixa un triangle equlàter d'una mida definida centrat al punt (x, y). La base es troba a la part inferior del triangle.'''
    goto_sense_dibuixar(x - (mida / 2), y + (mida * (math.sqrt(3) / 4)))
    for _ in range (3):
        forward (mida)
        right(120)

def dibuxa_triangles_fractals_invertits(mida: float, nivell: int, x: float, y: float) -> None:
    if nivell > 0:
        dibuxa_triange_invertit (mida / 2, x , y - (mida * (math.sqrt(3) / 8)))
        dibuxa_triangles_fractals_invertits (mida / 2, nivell - 1, x , y + (mida * (math.sqrt(3) / 8))) # Fractal superior
        dibuxa_triangles_fractals_invertits (mida / 2, nivell - 1, x + mida / 4 , y - (mida * (math.sqrt(3) / 8))) # Fractal inferior dreta
        dibuxa_triangles_fractals_invertits (mida / 2, nivell - 1, x - mida / 4, y - (mida * (math.sqrt(3) / 8))) # Fractal inferior esquerre

def main() -> None:
    mida = yogi.read(float)
    nivell = yogi.read(int)
    # Paràmetres de la tortuga
    hideturtle()
    speed(0)

    if nivell > 0:
        dibuxa_triange (mida, 0, 0)
        dibuxa_triangles_fractals_invertits (mida, nivell - 1, 0, 0)
    done ()

if __name__ == "__main__":
    main()