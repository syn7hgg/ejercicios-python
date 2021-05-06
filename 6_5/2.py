num = int(input("Ingrese un número: "))
cont = 1
try:
    file = open("EJ01-tabla-" + str(num) + ".txt", "r")
    while cont < 101:
        print(file.readline(), end="")
        cont += 1
except FileNotFoundError:
    print("El archivo no existe.")