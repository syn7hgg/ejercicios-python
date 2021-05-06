n = int(input("Ingrese un número: "))
m = int(input("Ingrese la línea a leer: ")) - 1
found = False
try:
    file = open("EJ01-tabla-" + str(n) + ".txt", "r")
    try:
        for pos, line in enumerate(file):
            if pos == m:
                print(line)
                found = True
                break
        if not found:
            print("No encontré esa línea.")
    except:
        print("Ocurrió un error.")
except FileNotFoundError:
    print("El archivo no existe.")
