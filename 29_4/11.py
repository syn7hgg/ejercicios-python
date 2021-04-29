def espar(n):
    if n % 2 == 0:

        return True

    else:

        return False


numeros = [1, 2, 3, 4, 5]

pares = list(filter(espar, numeros))

print(pares)
