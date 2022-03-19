def zakupy(słownik):
    print("Ilość produktów w koszyku: " + str(len(słownik)))
    lista = []
    for ket, value in słownik.items():
        lista.append(float(value))
    print(lista)


zakupowySłownik = {"mleko": "2,54", "ziemniaki": "13.54", "chleb": "1.9", "slodycze": "14.55"}

zakupy(zakupowySłownik)
