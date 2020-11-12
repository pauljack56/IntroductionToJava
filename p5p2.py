import sys
import math

userInput = int(sys.argv[1])
isValidInput = not math.isnan(userInput)
if(isValidInput):
    if(userInput < 0 ):
        print("you have input a negative number")
    else:
        print("you have input a non-negative number")

