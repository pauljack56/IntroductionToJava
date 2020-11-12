import sys
import math

userInput = float(sys.argv[1])
isNumber = not math.isnan(userInput)
if(isNumber):
    if(userInput < 0 ):
        print("you have input a negative number")

