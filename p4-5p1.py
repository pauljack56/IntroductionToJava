import sys
import math

amountEntered = float(sys.argv[1])
exchangeRate = float(sys.argv[2])
isValidInput = not math.isnan(amountEntered) and  not math.isnan(exchangeRate)
if(isValidInput):
    if(amountEntered < 0 or  exchangeRate < 0):
        print("Amounts must be >= 0. Please try again.")
    elif(amountEntered > 0 and  exchangeRate > 0):
        outputMessage = "Currency converted: " + str(amountEntered * exchangeRate)
        print(outputMessage)
    else:
        print("0")
else:
    print("you must enter numbers to convert")

