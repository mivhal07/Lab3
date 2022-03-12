def sprawdzenie(d, e, f):
    if (d * d) + (e * e) == (f * f):
        print("Jest to trójkąt")
    elif (d * d) + (f * f) == (e * e):
        print("Jest to trójkąt")
    elif (f * f) + (d * d) == (e * e):
        print("Jest to trójkąt")
    elif (f * f) + (e * e) == (d * d):
        print("Jest to trójkąt")


a = int(input("Wprowadź a: "))
b = int(input("Wprowadź b: "))
c = int(input("Wprowadź c: "))
sprawdzenie(a, b, c)
