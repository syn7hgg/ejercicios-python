from random import *

followUp = ""

while True:
    start = eval(input("Ingrese inicio: "))
    end = eval(input("Ingrese fin: "))
    floats = int(input("Ingrese cantidad de decimales: "))
    quant = int(input("Ingrese cantidad de números: "))
    name = input("Ingrese nombre de archivo: ")

    generated = []
    count = 0

    while count < quant:
        generated.append(str(round(uniform(start, end), floats)))
        count += 1

    try:
        file = open(name + ".txt", "a")
        for x in generated:
            file.write(x + "\n")
        file.close()
        print("Archivo guardado correctamente.")
    except:
        print("Ha ocurrido un error.")

    followUp = input("Si desea continuar, digite OK. Sino, digite cualquier otro caracter y presione ENTER: ")
    if followUp.upper() != "OK":
        break
