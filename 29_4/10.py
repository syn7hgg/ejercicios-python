def cuadrado(a):
    r = a * a

    return r


l = [1, 2, 3, 4, 5, 6, 7, 8]

cuadrados = map(cuadrado, l)

##print("resultado solo cuadrado: ", cuadrados)


for valor in cuadrados:
    print(valor)

lista_cuadrados = list(map(cuadrado, l))

print(lista_cuadrados)
