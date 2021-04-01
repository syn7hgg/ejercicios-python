print("Qué mes es?")

num = int(input("Ingresa un número del 1 al 12: "))

if num < 1 or num > 12:
    print("Fuera de rango.")
else:
    if num == 1:
        print("Es Enero.")
    elif num == 2:
        print("Es Febrero.")
    elif num == 3:
        print("Es Marzo.")
    elif num == 4:
        print("Es Abril.")
    elif num == 5:
        print("Es Mayo.")
    elif num == 6:
        print("Es Junio.")
    elif num == 7:
        print("Es Julio.")
    elif num == 8:
        print("Es Agosto.")
    elif num == 9:
        print("Es Septiembre.")
    elif num == 10:
        print("Es Octubre.")
    elif num == 11:
        print("Es Noviembre.")
    elif num == 12:
        print("Es Diciembre.")

# Termina el programa
print("-- PROGRAM END --")