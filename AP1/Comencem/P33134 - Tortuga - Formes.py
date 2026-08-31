from yogi import read
from turtle import *

forma = read (str)
mida1 = read (int)

if forma == "cercle":
    circle(mida1)

if forma == "quadrat":
    for i in range (4):
        forward (mida1)
        left (90)

if forma == "rectangle":
    mida2 = read (int)
    for i in range (2):
        forward (mida1)
        left(90)
        forward (mida2)
        left (90)

done ()
