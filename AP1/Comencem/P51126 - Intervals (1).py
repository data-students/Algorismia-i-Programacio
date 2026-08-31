from yogi import read

a1 = read (int)
b1 = read (int)
a2 = read (int)
b2 = read (int)

if (b1 < a2) or (b2 < a1):
    print ("[]")

elif a1 <= a2:
    if b1 <= b2:
        x = a2
        y = b1
    else:
        x = a2
        y = b2
    print ("[", x, "," , y, "]", sep = "") # Imprimir [x,y]
    
else:
    if b1 <= b2:
        x = a1
        y = b1
    else:
        x = a1
        y = b2

    print ("[", x, "," , y, "]", sep = "") # Imprimir [x,y]