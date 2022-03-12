from random import randint

lista1 = [randint(0, 100) for x in range(10)]
# for i in range(10):
#     a = randint(1, 100)
#     lista1.append(a)
print(lista1)

lista2 = [x for x in lista1 if x % 2 == 0]
# for i in lista1:
#     if i % 2 == 0:
#         lista2.append(i)
print(lista2)
