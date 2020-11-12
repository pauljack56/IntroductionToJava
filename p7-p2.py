"""
The leap year algorithm from Wikipedia:
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""

year = int(input('Enter a year\n>  '))
print(f"year entered = {year}")
commonYear = False
if year >= 0:
    if year % 4 != 0:
        commonYear = True
    elif year % 100 != 0:
        commonYear = False
    elif year % 400 == 0:
        commonYear = True
    else:
        commonYear = False
else:
    print("You need to input a number > 0 for the year")
if commonYear:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")
print("Finished!")
