from yogi import read

entrada = read(int)
n = entrada
digits = 0

if entrada == 0:
    print (0, end="")

while entrada // (10**digits) >= 1:
    digits += 1
    nreversed = (n % (10**digits)) // 10**(digits-1)
    n = n - (n % 10**digits)
    print (nreversed, end= "")

print ()

