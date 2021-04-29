from functools import reduce


def suma(a, b):
    return a + b


lista = [1, 2, 3, 4, 5, 6, 7]

print(reduce(suma, lista))
