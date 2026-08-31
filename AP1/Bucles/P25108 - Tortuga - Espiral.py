from yogi import read
from turtle import *

n = read(int)
m = read(int)
mida = m

for i in range (n):
    forward(mida)
    left (90)
    forward(mida)
    left (90)
    mida += m

done()