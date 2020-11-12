
cities = ["Dublin","Belfast","Cork","Limerick","Derry","Galway","Lisburn","Kilkenny","Waterford",  "Sligo"]

provinces= ["Leinster","Munster", "Ulster", "Connacht"]

province = {
    "Dublin":0,
    "Belfast":2,
    "Cork":1,
    "Limerick":1,
    "Derry":2,
    "Galway":3,
    "Lisburn":2,
    "Kilkenny":0,
    "Waterford":1,  
    "Sligo":3
}

for city in cities:
    provinceNum = province[city]
    cityProvince = provinces[provinceNum]
    print(f"elif(city === '{city}'):\n\tprint('{city} is in {cityProvince}')")