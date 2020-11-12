import sys
import math

programmeArguments = sys.argv
argc = len(programmeArguments)
programme_name = ""
input1 = None
input2 = None
if argc != 3:
    print("You need to pass 2 arguments to run this programme. Please try again")
    exit(0)

programme_name, input1, input2 = programmeArguments
firstNum = float(input1)
secondNum = float(input2)

if math.isnan(firstNum) or math.isnan(secondNum):
    print("you must enter 2 numbers as command line arguments for this programme to run")

sum = firstNum + secondNum
if sum > 100:
    print("That is a big number!")
    exit(0)
