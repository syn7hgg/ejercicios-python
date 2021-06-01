nombre = "solo_dolar.txt"


def archivo_ver(nombre):
    archivo = open(nombre, "r")

    datos = archivo.readlines()

    print("Inicio Lectura de Archivo ", nombre)

    for reg in datos:
        i = reg.split("\t")

        j = i[0]

        m = i[1]

        print("Para la fecha: ", j, " el valor del dólar es: ", m)

    return print("Fin Lectura de Archivo", nombre)


archivo_ver(nombre)
