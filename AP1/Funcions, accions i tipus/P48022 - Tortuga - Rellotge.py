from yogi import read
from turtle import penup, forward, backward, left, right, pendown, circle, goto, done

def dibuixa_rellotge() -> None:
    penup()
    forward(200)
    left(90)
    pendown()
    circle(200)  # Dibuixa el cerce del rellotge

    penup()
    goto(0, 0)
    pendown()  # Torna al centre del rellotge

    for i in range(12):  # Fa les 12 "ralletes" de les hores
        penup()
        forward(200)
        pendown()
        backward(50)
        penup()
        goto(0, 0)
        pendown()
        right(30)

def dibuixa_punta_busca() -> None:
    right(150)
    for i in range(3):  # Dibuixa la punta de la busca
        forward(25)
        right(120)

    left(150)

def dibuixa_hora(h:int, min: int) -> None:
    right((h / 12) * 360 + (min / 60) * (360 / 12))
    forward(90)  # Dibuixa la llargada de la busca de les hores

    dibuixa_punta_busca()

    penup()
    goto (0,0)
    pendown()
    left((h / 12) * 360 + (min / 60) * (360 / 12)) # La tortuga torna a mirar a les 12 h, en el centre del rellotje

def dibuixa_minuts(min: int) -> None:
    right(min / 60 * 360)
    forward(140)  # Dibuixa la llargada de la busca dels minuts

    dibuixa_punta_busca()

    penup()
    goto (0,0)
    pendown()
    left ((min / 60) * 360) # La tortuga torna a mirar a les 12 h, en el centre del rellotje


def main() -> None:
    e1, e2 = read(int), read(int)
    
    dibuixa_rellotge()
    dibuixa_hora(e1, e2)
    dibuixa_minuts(e2)
    
    done()

if __name__ == "__main__":
    main()