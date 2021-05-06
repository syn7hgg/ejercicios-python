num = int(input("Ingrese un número: "))
while num < 1 or num > 10:
    num = int(input("El número debe estar en el intervalo [1,10]: "))
count = 1

try:
    file = open("EJ01-tabla-" + str(num) + ".txt", "x")
    print("Archivo creado.")

    try:
        file = open("EJ01-tabla-" + str(num) + ".txt", "a")
        while count < 101:
            print("Agregando línea: " + str(num) + " x " + str(count) + " = " + str(num * count))
            file.write(str(num) + " x " + str(count) + " = " + str(num * count) + "\n")
            count += 1
        print("Archivo modificado exitosamente.")
    except FileNotFoundError:
        print("No he podido encontrar el archivo.")

except FileExistsError:
    print("El archivo ya existe.")
