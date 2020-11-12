import sys
import math

userInput = int(sys.argv[1])
isValidInput = not math.isnan(userInput)
if(isValidInput):
    if(userInput == 0):
        print("you have input a zero")
    elif(userInput in range(1,21)):
        print("0 > input <= 20 ")
    elif(userInput in range(20,41)):
        print("20 > input <= 40 ")
    elif(userInput in range(40,61)):
        print("40 > input <= 60 ")
    elif(userInput in range(60,81)):
        print("60 > input <= 80 ")
    elif(userInput in range(80,101)):
        print("80 > input <= 100 ")
    elif(userInput > 100):
        print("user input is greater than 100")
   


# reference where i read about the range object : https://stackoverflow.com/a/20623994/4020228