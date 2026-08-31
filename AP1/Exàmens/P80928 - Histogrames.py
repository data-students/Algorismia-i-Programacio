from turtle import goto, penup, pendown, forward, write, right, left, done
import yogi
from dataclasses import dataclass

@dataclass
class Numero:
    numero: int | float
    frequencia: int

def dibuixa_histograma (n: int, llista_barres: list[Numero], frequencia_maxima: int) -> None:

    # Posicionem la tortuga per centrar l'histograma
    penup()
    goto(-150, -150)
    pendown()

    # Escribim la base
    write (llista_barres[0].numero)
    for i in range(1, n + 1):
        forward(300 / n)
        write (llista_barres[i].numero)
    goto(-150, -150)

    # Escribim les barres
    for i in range(n):
        left(90)
        forward(llista_barres[i].frequencia / frequencia_maxima * 300)
        right(90)
        forward(300 / n)
        right(90)
        forward(llista_barres[i].frequencia / frequencia_maxima * 300)
        left(90)
    return

def calcula_barres (n: int, llista_frequencies: list[Numero]) -> tuple[list[Numero], int]:
    '''Donada una llista de frequencies, crea n barres corresponents a les frequencies donades.'''

    numero_maxim = llista_frequencies[-1].numero
    barra_frequencia = 0
    frequencia_maxima = 0
    diferencia = (numero_maxim) / (n)
    llista_barres = [Numero(round(diferencia*i, 1), 0) for i in range(n + 1)]
    i = 0
    for numero in llista_frequencies:
        if numero.numero >= llista_barres[i + 1].numero:
            i += 1
            if barra_frequencia > frequencia_maxima:
                frequencia_maxima = barra_frequencia
            barra_frequencia = 0
        barra_frequencia += numero.frequencia
        llista_barres[i].frequencia += numero.frequencia
    
    return llista_barres, frequencia_maxima

def llegir_frequencia_entrades() -> list[Numero]:

    llista_frequencies: list[Numero] = []
    llista_numeros = [numero for numero in yogi.tokens(int)]
    llista_numeros.sort()

    numero_ant = i = -1
    for numero in llista_numeros:
        if numero != numero_ant:
            llista_frequencies.append(Numero(numero, 1))
            i += 1
        else:
            llista_frequencies[i].frequencia += 1
        numero_ant = numero
    
    return llista_frequencies

def main() -> None:
    n = yogi.read(int)
    llista_frequencies = llegir_frequencia_entrades()
    llista_barres, frequencia_maxima = calcula_barres(n, llista_frequencies)
    print (llista_barres)
    dibuixa_histograma (n, llista_barres, frequencia_maxima)
    done()

if __name__ == "__main__":
    main()
