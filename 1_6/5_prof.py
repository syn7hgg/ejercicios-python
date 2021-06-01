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

    # print("\nInicio Lectura de Archivo para determinar el valor promedio del Dólar", nombre)

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


def separar_promedio(nombre):
    promedio = promedio_valor(nombre)

    archivo = open(nombre, "r")

    datos = archivo.readlines()

    archivo_ma = open("dolar_mayor_prom.txt", "w")

    archivo_me = open("dolar_menor_prom.txt", "w")

    print("\n.... Se comienza a generar los archivos ....")

    for reg in datos:

        i = reg.split("\t")

        j = i[0]

        num = i[1]

        if float(num) >= promedio:

            linea = j + "\t" + num

            archivo_ma.write(linea)

        else:

            linea = j + "\t" + num

            archivo_me.write(linea)

    print("Archivo %s con valor dólar mayor igual al promedio %.2f GENERADO" % ("dolar_mayor_prom.txt", promedio))

    print("Archivo %s con valor dólar menor al promedio %.2f GENERADO" % ("dolar_menor_prom.txt", promedio))

    return print(".... Termino de generación de los archivos ....")


archivo_ver(nombre)

maximo_valor(nombre)

print("\nEl promedio del Dólar es: ", promedio_valor(nombre))

separar_promedio(nombre)


def ordenar_mayor_a_menor(nombre):
    archivo = open(nombre + ".txt", "r")

    archivo_s = open(nombre + "_ordmayor.txt", "w")

    datos2 = archivo.readlines()

    print("\n.... Se comienza a generar los archivos ordenados de mayor a menor....")

    maximo_valor = None

    z = 0

    datos = datos2

    while z < len(datos2):

        for reg in datos:

            i = reg.split("\t")

            j = i[0]

            num = i[1]

            if (maximo_valor is None or num > maximo_valor):
                maximo_valor = num

                fecha = j

                # print("j",j,"num",num)

                # linea=fecha+","+maximo_valor

                # archivo_s.write(linea)

        limpio = maximo_valor.strip()

        limpio = str(limpio)

        linea = fecha + "," + maximo_valor

        # print("linea",linea)

        archivo_s.write(linea)

        # print("antes",len(datos))

        datos.remove(fecha + "\t" + maximo_valor)

        # print("despues",len(datos))

        # print(limpio)

        limpio = ""

        # print(limpio)

        maximo_valor = None

        # z+=1

    return print(".... Termino de generación de archivo Ordenados ....")


archivo_ver(nombre)

maximo_valor(nombre)

print("\nEl promedio del Dólar es: ", promedio_valor(nombre))

separar_promedio(nombre)

ordenar_mayor_a_menor("dolar_mayor_prom")

ordenar_mayor_a_menor("dolar_menor_prom")
