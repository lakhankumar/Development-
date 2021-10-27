import random

def flipCoin():
    head = 0 
    tail = 0
    n = int(input("enter the number of times you want to flip coin: "))
    if n > 0:
        for i in range(n):
            coin = random.randint(0,1)
            if coin == 0:
                head += 1
            else:
                tail += 1

        headPercent = ((head/(head + tail))*100)
        tailPercent = ((tail/(head + tail))*100)
        print("Head percentage = " ,headPercent)
        print("tail percentage = " ,tailPercent)
    else:
        print("Enter positve integer")

flipCoin()