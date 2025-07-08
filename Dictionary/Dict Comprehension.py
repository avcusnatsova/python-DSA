import random

city_name = ['paris', 'rome', 'delhi', 'melbourne']

city_temp = {city:random.randint(20,30) for city in city_name}

grt = {city: temp for (city,temp) in city_temp.items() if temp > 25}
print(grt)