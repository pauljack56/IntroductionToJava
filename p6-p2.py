import sys
import math

programmeArguments = sys.argv
argc = len(programmeArguments)
programme_name = ""
input1 = None
input2 = None
if argc != 4:
    print("You need to pass 3 arguments to run this programme. Please try again")
    exit(0)

programme_name, input1, input2, input3 = programmeArguments
firstNum = int(input1)
secondNum = int(input2)
thirdNum = int(input3)

if math.isnan(firstNum) or math.isnan(secondNum) or math.isnan(thirdNum):
    print("you must enter 3 numbers as command line arguments for this programme to run")

firstNumOdd = firstNum % 2 == 1
secondNumOdd = secondNum % 2 == 1
thirdNumOdd = thirdNum % 2 == 1

hasOddInput = firstNumOdd or secondNumOdd or thirdNumOdd

if not hasOddInput:
    print("no odd input detected")
    exit(0)

outputNumber = math.inf * -1
if firstNumOdd:
    outputNumber = firstNum
if secondNumOdd and secondNum > outputNumber:
    outputNumber = secondNum
if thirdNumOdd and thirdNum > outputNumber:
    outputNumber = thirdNum

print(f"the largest odd number that you input was {outputNumber}")
