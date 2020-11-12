import sys
import math

sideLength = float(sys.argv[1])
isValidInput = not math.isnan(sideLength)
if(isValidInput):
    if(sideLength < 0):
        print("Length must be >= 0. Try again")
    else:
        print("With the given side length:")
        print("Area of a square : "+str(sideLength*sideLength)) #l^2
        print("Volume of cube : "+ str(math.pow(sideLength,3))) #l^3
        print("Area of circle (with given radius) : "+ str(math.pi*math.pow(sideLength,2))) # pi*r^2
        print("Volume of sphere (with given radius) : "+ str((4.0/3.0) * math.pi*math.pow(sideLength,3))) # 4/3 * pi * r^3
        print("Volume of cylinder (height and radius equal given length) : " + str(math.pi*math.pow(sideLength,2)*sideLength)) # pi * r^2 * h