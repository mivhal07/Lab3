karta = {"Gruszki": "Kg",
         "Jabłka": "Kg",
         "Ogórek": "Szt",
         "Pomidor": "Szt",
         "Czosnek": "Szt"}

lista = []
for key, value in karta.items():
    if key == "Szt":
        lista.append(value)
print(lista)
