import sys
import math

userInput = float(sys.argv[1])
isValidInput = not math.isnan(userInput)
if(isValidInput):
    if(userInput < 0 ):
        print("you have input a negative number")
    elif(userInput > 0):
        print("you have input a positive number")
    else:
        print("you have input a zero")

