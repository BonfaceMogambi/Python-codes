import math
int = float (input("Please input a number: "))

if int <= 0:
    raise Exception("The number can't be less than or equal to zero")
else:
    y = math.sqrt(int)
    print (f"You entered {int} as your lucky number")
    print (f"The square root of {int} is {y}")
    print ("Have a nice day!")