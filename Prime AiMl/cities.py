import json

# cities = {
#   "Agra" : 1299,
#   "Delhi": 3902,
#   "Jaipur": 2984
# }
# with open("cities.json" , "w")as f:
#     json.dump(cities, f, indent = 4)

with open("cities.json") as f:
    data = json.load(f)

new_city = input("Enter new city :")
new_popln = int(input("Enter population:"))

data[new_city] = new_popln

with open("cities.json", "w") as f:
    json.dump(data, f, indent = 4)

print(new_city, new_popln)

