import random

a = int(input("ingrese N de la Matriz: "))

b = int(input("ingrese M de la Matriz: "))

nombre = "matriz_n_por_n"


def matriz_base(n, m):
    matriz = []

    for i in range(n):
        a = [0] * m

        matriz.append(a)

    return matriz


def matriz_random(matriz):
    for i in range(len(matriz)):

        for k in range(len(matriz[i])):
            matriz[i][k] = round(random.uniform(0, 10), 2)

    return matriz


def mostrar(matriz):
    print("La matriz es la siguiente:")

    for fila in matriz:

        for valor in fila:
            print("\t", valor, end=" ")

        print()

    return print("Fin de Lectura")


def grabar(matriz):
    archivo = open(nombre + '.txt', 'w')

    linea = []

    for fila in matriz:

        for valor in fila:
            valor = str(valor)

            linea.append(valor)

            # print(linea)

        line = " ".join(linea)

        # print(line)

        archivo.write(line + "\n")

        linea = []

    archivo.close()

    return print(" Grabación OK")


def lectura(nombre):
    archivo = open(nombre + '.txt', 'r')

    matrix = archivo.readlines()

    # print(matrix)

    print("Inicio Lectura de Archivo")

    for reg in matrix:

        i = reg.split(" ")

        for j in i:
            print("\t", j, end=" ")

    return print("Fin Lectura de Archivo")


c = matriz_base(a, b)

d = matriz_random(c)

mostrar(d)

grabar(d)

lectura(nombre)
