currentNum = 0
total = 0
while currentNum <= 10000:
    if currentNum % 3 == 0 or currentNum % 5 == 0:
        total = total + currentNum;
    currentNum = currentNum + 1
print(f"Total\t{total}")
