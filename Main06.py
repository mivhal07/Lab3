def ciąg(a1, b, ile):
    ilosc = a1 + ile;
    # a10 = 1 + 9 * 4
    # a9 = 1 + 8 * 4
    # a3 = 1 + 2 * 4
    # a2 = 1 + 1 * 4
    # a1 = 1
    result = 0
    for x in range(a1, ilosc):
        result += x + (x - 1) * b
        return result


print(ciąg(1, 4, 10))
