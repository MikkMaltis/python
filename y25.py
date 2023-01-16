thisdict = {
    "first_name": "Mikk",
    "surname": "Maltis",
    "year_of_birth": 2006,
    "place_of_residence": "Muhu"
    "favourite_dessert": "caramel pudding"
}

print(me.get("place_of_residence"))
print(me["place_of_residence"])

me["favourite_dessert"] = "caramel pudding"

for k, v in me.items():
    print(k, v)