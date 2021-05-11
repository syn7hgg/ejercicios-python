def Menu():
    """Funcion que Muestra el Menu"""

    print("""************

Calculadora



************



Menu



1) Suma



2) Resta



3) Multiplicacion



4) Division



5) Salir""")


def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""

    Menu()

    print("----------------------------")

    opc = int(input("Selecione Opcion: "))

    while (opc > 0 and opc < 5):

        x = int(input("Ingrese Numero: "))

        y = int(input("Ingrese Otro Numero: "))

        if (opc == 1):

            print("La Suma es:", x + y)

            Menu()

            opc = int(input("Selecione Opcion: "))

        elif (opc == 2):

            print("La Resta es:", x - y)

            Menu()

            opc = int(input("Selecione Opcion: "))

        elif (opc == 3):

            print("La Multiplicacion es:", x * y)

            Menu()

            opc = int(input("Selecione Opcion: "))

        elif (opc == 4):

            try:

                print("La Division es:", x / y)

                Menu()

                opc = int(input("Selecione Opcion: "))

            except ZeroDivisionError:

                print("No se Permite la Division Por 0")

                Menu()

                opc = int(input("Selecione Opcion: "))


Calculadora()
