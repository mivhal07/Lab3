def ciąg(a1, b, ile):
    ilosc = a1 + ile - 1
    result = 1
    for x in range(ilosc):
        print(result)
        result *= b


ciąg(1, 2, 10)
