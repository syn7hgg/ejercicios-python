print("Qué día es?")

num = int(input("Ingresa un número del 1 al 7: "))

if(num < 1 or num > 7):
    print("Fuera de rango.")
else:
    if num == 1:
        print("Es Lunes.")
    elif num == 2:
        print("Es Martes.")
    elif num == 3:
        print("Es Miércoles.")
    elif num == 4:
        print("Es Jueves.")
    elif num == 5:
        print("Es Viernes.")
    elif num == 6:
        print("Es Sábado.")
    elif num == 7:
        print("Es Domingo.")

# Termina el programa
print("-- PROGRAM END --")