while True:

    nombre = input("Ingrese nombre de archivo sin ext. : ")

    try:

        arch = open(nombre + '.txt', 'r')

    except FileNotFoundError:

        print("archivo no existe")

        crear = input("digite OK si desea cear el archivo: ")

        if crear == "OK":

            arch = open(nombre + '.txt', 'w')

        else:

            continue

    break

while True:

    print("-- 1: Ingreso de artículo")

    print("-- 2: Consulta de un artículo")

    print("-- 3: Consulta de artículo")

    print("-- 4: salir")

    opc = input("Seleccione una opción: ")

    if opc == "1":

        arch = open(nombre + '.txt', 'a')

        cod = int(input("Ingrese código: "))

        cant = int(input("Ingrese cantidad: "))

        pre = float(input("Ingrese precio: "))

        nom = input("Ingrese nombre: ")

        linea = str(cod) + "," + str(cant) + "," + str(pre) + "," + nom + "\n"

        arch.write(linea)

        arch.close()

    elif opc == "2":

        arch = open(nombre + '.txt', 'r')

        linea = arch.readline()

        xcod = int(input("ingresa el código : "))

        exito = False

        while linea != "":

            reg = linea.split(",")

            cod = int(reg[0])

            cant = int(reg[1])

            pre = float(reg[2])

            nom = reg[3]

            if xcod == cod:
                print("Cantidad: ", cant)

                print("Precio: ", pre)

                print("Nombre: ", nom)

                exito = True

                break

            linea = arch.readline()

        if not exito:
            print("No existe el registro")

        arch.close()

    elif opc == "3":

        archivo = open(nombre + '.txt', 'r')

        B = archivo.readlines()

        for i in range(len(B)):

            for k in range(len(B[i])):
                print(B[i][k], end="")

        print()

    elif opc == "4":

        print("Muchas Gracias")

        break
