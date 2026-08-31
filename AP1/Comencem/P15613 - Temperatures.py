import yogi

temp = yogi.read (int)

if temp > 30:
    print ("it's hot")
    if temp >= 100:
        print ("water would boil")

elif temp < 10:
    print ("it's cold")
    if temp <= 0:
        print ("water would freeze")

else:
    print("it's ok")