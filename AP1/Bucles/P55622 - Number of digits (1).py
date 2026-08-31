from yogi import read

n = read(int)

i = 1

while n // (10**i) >= 1:
    i += 1

print (f'The number of digits of {n} is {i}.')