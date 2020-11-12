import sys
import math

grossIncome = float(sys.argv[1])
if(math.isnan(grossIncome) or grossIncome < 0):
    print("Amount of income must be >= 0. Please try again")
    exit(0)

grossBand1 = grossIncome * 0.6
grossBand2 = grossIncome * 0.4
netBand1 = grossBand1 * 0.77
netBand2 = grossBand2 * 0.59
netIncome = netBand1 + netBand2

print("gross income : "+ str(grossIncome))
print(f"lower tax band (calculated as follows): {grossBand1} - {grossBand1 - netBand1} = {round(netBand1,2)}")
print(f"upper tax band (calculated as follows): {grossBand2} - {grossBand2 - netBand2} = {round(netBand2,2)}")
print(f"total tax due {round(grossIncome - netIncome,2)}")
print("--------------------------")
print(f"net income : {round(netIncome,2)}")

# reference : round function. Stack Overflow. https://stackoverflow.com/a/20457115/4020228