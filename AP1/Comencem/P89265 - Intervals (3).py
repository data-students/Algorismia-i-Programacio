from yogi import read

a1 = read (int)
b1 = read (int)
a2 = read (int)
b2 = read (int)

# Bloque 1

if (a1 == a2) and (b1 == b2):
    print ("=", end = "")

elif a2 <= a1 <= b1 <= b2:
    print ("1", end = "")

elif a1 <= a2 <= b2 <= b1:
    print ("2", end = "")

else:
    print ("?", end = "")

# Enlace con el bloque 2
print (" , ", end = "")

# Bloque 2

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