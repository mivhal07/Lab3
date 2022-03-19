import random

plik = open("plik.txt", "r+")

lista = []
for x in range(100):
    if x % 4 == 0:
        lista.append(x)
plik.write(str(lista))
