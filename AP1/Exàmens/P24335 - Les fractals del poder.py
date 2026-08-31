import yogi
from turtle import penup, pendown, goto, done, speed, hideturtle

def goto_sense_pintar (x: float, y: float) -> None:
    '''Funció que mou a la tortuga al punt (x, y) sense pintar res pel camí.'''

    penup()
    goto(x,y)
    pendown()

def dibuixa_quadrat (mida: float, x: float, y: float) -> None:
    '''Funció que dibuixa un quadrat d'una certa mida centrat al punt (x, y)'''
    goto_sense_pintar (x + mida / 2, y - mida / 2)
    goto (x - mida / 2, y - mida / 2)
    goto (x - mida / 2, y + mida / 2)
    goto (x + mida / 2, y + mida / 2)
    goto (x + mida / 2, y - mida / 2)

def dibuixa_quadrats_fractals (mida: float, nivell: int, x: float, y: float) -> None:
    '''Dibuixa un fractal de quadrats d'una certa mida centrat al punt (x, y)'''
    dibuixa_quadrat(mida, x, y)
    if nivell != 1:
        dibuixa_quadrats_fractals (mida / 3, nivell - 1, x + mida, y - mida)
        dibuixa_quadrats_fractals (mida / 3, nivell - 1, x - mida, y - mida)
        dibuixa_quadrats_fractals (mida / 3, nivell - 1, x - mida, y + mida)
        dibuixa_quadrats_fractals (mida / 3, nivell - 1, x + mida, y + mida)

def main() -> None:
    mida = yogi.read(float)
    nivells = yogi.read(int)
    
    # Paràmetres de la tortuga
    hideturtle()
    speed(0)

    dibuixa_quadrats_fractals (mida, nivells, 0, 0)
    done()

if __name__ == "__main__":
    main()
