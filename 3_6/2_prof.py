def separar_meses_sol1(nombre):
    archivo = open(nombre, "r")

    datos = archivo.readlines()

    print("\n.... Se comienza a generar los archivos por meses sol1....")

    L = []

    L2 = []

    z = 1

    for reg in datos:

        i = reg.split("\t")

        j = i[0]

        num = i[1]

        L.append(j[3:9])

        L2 = list(set(L))

        for mes in (L2):

            if j[3:9] == mes:
                linea = j + "@" + num

                nombre_arch = open("sol1" + mes + ".txt", "a")

                nombre_arch.write(linea)

    nombre_arch.close()

    return print("### Archivo OK ###")


def separar_meses_sol2(nombre):
    archivo = open(nombre, "r")

    datos = archivo.readlines()

    L = []

    L2 = []

    z = 0

    print("\n.... Se comienza a generar los archivos por meses sol2....")

    for reg in datos:
        i = reg.split("\t")

        j = i[0]

        num = i[1]

        L.append(j[3:9])

        L2 = list(set(L))

        L2 = list(L2)

        L3 = L2

    while z < len(datos):

        for mes in (L2):

            if datos[z][3:9] == mes:
                linea = datos[z]

                nombre_arch = open(mes + ".txt", "a")

                nombre_arch.write(linea)

        z += 1

    nombre_arch.close()

    return print("### Archivo OK ###")
