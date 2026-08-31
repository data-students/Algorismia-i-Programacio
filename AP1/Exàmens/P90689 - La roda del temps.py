import yogi
from turtle import circle, penup, pendown, goto, speed, hideturtle, done

def dibuixa_cercle (x: float, y: float, mida: float) -> None:
    '''Dibuixa un cercle de amb radi "mida" centrat al punt ("x", "y")'''

    penup()
    goto (x, y - mida) # La tortuga comença a dibuixar desde la part més baixa del cercle
    pendown()

    circle (mida)

def dibuixa_cercles_fractals (x: float, y: float, mida: float, nivell: int) -> None:
    '''Dibuixa cercles fractals de radi "mida" i centrat al punt ("x", "y")'''

    if nivell <= 0:
        return
    # Cas base, on es dibuixarà sempre un cercle al nivell més exterior
    dibuixa_cercle(x, y, mida) 

    # Cas "inductiu" on, en cas de que no sigui el nivell més baix de fractal, es 
    # dibuixarán dos cercles més petits dins del més gran.
    if nivell > 1: 
        dibuixa_cercle(x, y, mida)
        dibuixa_cercles_fractals(x + mida / 2, y, mida / 2, nivell - 1)
        dibuixa_cercles_fractals(x - mida / 2, y, mida / 2, nivell - 1)

def main() -> None:
    # Entrada de les dades
    mida = yogi.read(float)
    nivells = yogi.read(int)

    # Paràmetres per la tortuga
    speed (0)
    hideturtle()

    dibuixa_cercles_fractals (0,0, mida, nivells)

    done()

if __name__ == "__main__":
    main()