import random

a = int(input("ingrese N de la Matriz: "))

b = int(input("ingrese M de la Matriz: "))

nombre = str(input("ingrese nombre del archivo: "))


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

    return print(" Grabación OK archivo ", nombre + ".txt")


def lectura(nombre):
    archivo = open(nombre + '.txt', 'r')

    matrix = archivo.readlines()

    # print(matrix)

    print("Inicio Lectura de Archivo ", nombre + ".txt")

    for reg in matrix:

        i = reg.split(" ")

        for j in i:
            print("\t", j, end=" ")

    return print("Fin Lectura de Archivo", nombre + ".txt")


def cambio(d, a, b):
    i = random.randint(0, a - 1)

    j = random.randint(0, b - 1)

    # print("a-i b-j",a,i,b,j)

    d[i][j] = random.randint(0, 10)

    print("cambio de valor en la posición n=%d , m=%d por %d" % (i + 1, j + 1, d[i][j]))

    return d


c = matriz_base(a, b)

d = matriz_random(c)

mostrar(d)

cambio(d, a, b)

print("cambio de matriz")

mostrar(d)

grabar(d)

lectura(nombre)
