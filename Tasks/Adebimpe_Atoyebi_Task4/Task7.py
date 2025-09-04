cities = ["Jos", "Ikeja", "Sango", "Ife", "Ifo"]
nCity = input("Enter a new city: ")
cities.insert(2, nCity)
# print(cities)
removeLastCity = cities.pop()
# print(cities)
cities.insert(0, "Yaba")
print(cities)

