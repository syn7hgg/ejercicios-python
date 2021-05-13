import numpy

import random

lista_matriz = ["array1", "array2", "array3"]


def matrix(a, b):
    random_float_array = numpy.random.rand(a, b)

    return random_float_array


def matrix_nombre(lista_matriz):
    r = random.choice(lista_matriz)

    return r


def matrix_archivo(a):
    nombre = matrix_nombre(lista_matriz)

    arch = open(nombre + '.txt', 'w')

    for i in a:
        arch.write(str(i) + "\n")

    arch.close()

    return print("grabación ok en archivo ", nombre + ".txt"), print(
        "\nel archivo quedo con los siguientes registros\n"), matrix_lectura(nombre)


def matrix_lectura(nombre):
    p = []

    # print(nombre)

    arch2 = open(nombre + '.txt', 'r')

    data = arch2.readlines()

    # print(data)

    for i in range(len(data)):

        for j in range(len(data[i])):
            print((data[i][j]), end="")

    return print("\nFin de lectura de archivo ", nombre + '.txt')


def inicio():
    print("Matriz de N x M")

    n = int(input("ingrese N: "))

    m = int(input("ingrese M: "))

    a = matrix(n, m)

    print(a, "\n")

    matrix_archivo(a)


inicio()
