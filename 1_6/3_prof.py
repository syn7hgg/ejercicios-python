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


def maximo_valor(nombre):
    archivo = open(nombre, "r")

    datos = archivo.readlines()

    print("\nInicio Lectura de Archivo para determinar el valor máximo del Dólar y su fecha", nombre)

    maximo_valor = None

    for reg in datos:

        i = reg.split("\t")

        j = i[0]

        num = i[1]

        if (maximo_valor is None or num > maximo_valor):
            maximo_valor = num

            fecha = j

    limpio = maximo_valor.strip()

    limpio = str(limpio)

    # l=datos.index(maximo_valor)

    # print(l)

    return print("Máximo valor del Dólar es: ", limpio, "que corresponde a la fecha: ", fecha)


def promedio_valor(nombre):
    archivo = open(nombre, "r")

    datos = archivo.readlines()

    print("\nInicio Lectura de Archivo para determinar el valor promedio del Dólar", nombre)

    suma = 0

    contador = 0

    for reg in datos:
        i = reg.split("\t")

        j = i[0]

        num = i[1]

        suma += float(num)

        contador += 1

        # print(suma,contador)

    promedio = round(suma / contador, 2)

    return promedio


archivo_ver(nombre)

maximo_valor(nombre)

print("El promedio del Dólar es: ", promedio_valor(nombre))
