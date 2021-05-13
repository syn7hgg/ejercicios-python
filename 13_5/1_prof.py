import random


def get_float_list(start, stop, size, dec):
    result = []

    unique_set = set()

    for i in range(size):

        x = round(random.uniform(start, stop), dec)

        while x in unique_set:
            x = round(random.uniform(start, stop), dec)

        unique_set.add(x)

        result.append(x)

    return result


def en_archivo(nom, result):
    arch = open(nom + '.txt', 'w')

    for i in result:
        arch.write(str(i) + "\n")

    return print("Archivo grabado....OK")


def inicio():
    while True:

        z = str(input("si desea continuar digite OK sino presiones SALIR "))

        if z == "OK":

            print("Lista de números random")

            inicio = int(input("ingrese inicio: "))

            fin = int(input("ingrese fin: "))

            dec = int(input("ingrese la cantidad de digitos decimales: "))

            cant = int(input("ingrese cantidad de números: "))

            nom = str(input("ingrese nombre de archivo: "))

            result = (get_float_list(inicio, fin, cant, dec))

            print(result)

            en_archivo(nom, result)

        elif z == "SALIR":

            break


try:

    inicio()

except:

    print("ingrese opción valida")

    inicio()
