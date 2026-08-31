from yogi import read

a, b = read(int), read(int)

# Versión 2
i = 1
gcd = 1

while i*i <= a:
    if a % i == 0:
        div1 = i
        div2 = a // i
        if b % div1 == 0:
            if gcd < div1:
                gcd = div1
        if b % div2 == 0:
            if gcd < div2:
                gcd = div2
    
    i += 1

print (f'The gcd of {a} and {b} is {gcd}.')
