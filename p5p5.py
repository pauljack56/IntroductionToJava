import sys
import math

userInput = sys.argv[1]
city = ""
if(isinstance(userInput, str)):
    city = userInput

if(city == 'Dublin'):
    print('Dublin is in Leinster')
elif(city == 'Belfast'):
    print('Belfast is in Ulster')
elif(city == 'Cork'):
    print('Cork is in Munster')
elif(city == 'Limerick'):
    print('Limerick is in Munster')
elif(city == 'Derry'):
    print('Derry is in Ulster')
elif(city == 'Galway'):
    print('Galway is in Connacht')
elif(city == 'Lisburn'):
    print('Lisburn is in Ulster')
elif(city == 'Kilkenny'):
    print('Kilkenny is in Leinster')
elif(city == 'Waterford'):
    print('Waterford is in Munster')
elif(city == 'Sligo'):
    print('Sligo is in Connacht')
else:
    print("Sorry I didn't recognise the name")
   