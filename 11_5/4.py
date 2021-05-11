# Calculadora

num1, num2, sel = 0, 0, 0


def add():
    global num1, num2
    print("La suma de", num1, "+", num2, "es:", num1 + num2)


def sub():
    global num1, num2
    print("La resta de", num1, "-", num2, "es:", num1 - num2)


def mult():
    global num1, num2
    print("La multiplicación de", num1, "x", num2, "es:", num1 * num2)


def div():
    global num1, num2
    print("La división de", num1, "/", num2, "es:", num1 / num2)


print("< =========== >")
print("< Calculadora >")
print("< =========== >")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")
print("< =========== >")

while True:
    try:
        sel = int(input("Selecciona una operación: "))
        if sel < 1 or sel > 4:
            print("Hasta luego!")
            break
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("Debe ser un número entero.")

    if sel == 1:
        add()
    elif sel == 2:
        sub()
    elif sel == 3:
        mult()
    elif sel == 4:
        div()
