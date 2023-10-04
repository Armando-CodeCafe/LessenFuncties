import json
dct = {
    "Mx5":"Mazda",
    "GT Skyline":"Nissan",
    "Veyron":"Bugatti",
    "ABC":["Honda","Toyota"]
}

telefoonboek = {
    ("Armando","Roerdinkveldboom"):"0611084938",
    ("Henk","de Tank"):"0612385989",
    ("Anna","Masala"):"0612345789"
}

def lookup(dict):
    name = input("Voornaam: ")
    last_name = input("Achternaam: ")
    tup = (name,last_name)
    print(dict[tup])

#lookup(telefoonboek)

#file = open("test.json","r")
#doe code
#file.close()
#zelfde als:
# with open("test.json","r") as file:
#     data = json.load(file)
#     for persoon in data["employees"]:
#         if persoon["name"][0].upper() == "A": #print alleen mensen met een A als voornaam
#             print(persoon)

with open("test.json","r") as file:
    print(type(json.load(file)["Veyron"]))