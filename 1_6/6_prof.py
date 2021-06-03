def ordenar_menor_a_mayor(nombre):
    archivo = open(nombre + ".txt", "r")

    archivo_s = open(nombre + "_ord_demenor.txt", "w")

    datos2 = archivo.readlines()

    print("\n.... Se comienza a generar los archivos ordenados de menor a mayor ....")

    minimo_valor = None

    z = 0

    datos = datos2

    while z < len(datos2):

        for reg in datos:

            i = reg.split("\t")

            j = i[0]

            num = i[1]

            if (minimo_valor is None or num < minimo_valor):
                minimo_valor = num

                fecha = j

        limpio = minimo_valor.strip()

        limpio = str(limpio)

        linea = fecha + "," + minimo_valor

        archivo_s.write(linea)

        datos.remove(fecha + "\t" + minimo_valor)

        limpio = ""

        minimo_valor = None

    archivo_s.close()

    return print(".... Termino de generación de archivo Ordenados ....")
