def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
'''
from yogi import read
a = read(int)
b = read(int)
print(gcd(a,b))
'''
