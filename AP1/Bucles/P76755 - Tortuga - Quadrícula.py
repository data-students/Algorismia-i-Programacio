from yogi import read
from turtle import *

n, m = read (int), read (int)

for j in range (2):
    for i in range (n):
        left(90)
        forward(m*n)
        right(90)
        forward(m)
        right(90)
        forward(m*n)
        left(90)

    left (90)

done()