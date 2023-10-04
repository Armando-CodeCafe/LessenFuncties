import json
dct = { #key = model, value is merk
    "Mx5":["Mazda","Nissan","Citroen"],
    "Veyron":"Bugatti",
    "Agera":"Koenigsegg",
    "M5CS":"BMW",
    "A8":"Audi"
}
motordealer = {
    "Ninja 650R":"Kawasaki",
    "GTS300": "Vespa",
    "Versys 300":"Kawasaki"
}

telefoonboek={
    ("Armando","Roerdinkveldboom"):"0611084938",
    ("Henk","de Tank"):"0612345678",
    ("Lars","Tokkie"):"0642069123"
}

def lookup(dct):
    naam = input("Naam: ")
    achter= input("Achternaam: ")
    tup = (naam,achter)
    if tup in dct:
        print(dct[tup])
    else:
        print("Niet een bestaande naam")

with open("namen.json","w") as file:
    json.dump(dct,file)

