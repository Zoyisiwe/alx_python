
import random
number = random.randint(-10, 10)

if number < 0:
    print( number ,"is positive" ,end="\n")

elif number == 0:
    print(number, "is 0" , end="\n")

else:
    print ( number, "is negative" , end="\n")

