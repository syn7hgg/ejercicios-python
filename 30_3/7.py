from math import factorial, sqrt

print("=== Calculadora by Andrés ===")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Residuo")
print("7. Factorial")
print("8. Raíz cuadrada")
print("=============================")

# Valores por defecto (FALLBACK)
n1 = 0
n2 = 0
num = 0

sel = int(input("Ingrese la operación deseada: "))
if sel < 1 or sel > 8:
    print("Operación inválida, se espera un rango 1-8")
else:
    if sel > 0 and sel < 7:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
    else:
        num = float(input("Ingrese un número: "))

    if sel == 1:
        res = n1 + n2
        if res.is_integer():
            res = int(res)
        print(n1, "+", n2, "=", res)

    elif sel == 2:
        res = n1 - n2
        if res.is_integer():
            res = int(res)
        print(n1, "-", n2, "=", res)

    elif sel == 3:
        res = n1 * n2
        if res.is_integer():
            res = int(res)
        print(n1, "*", n2, "=", res)

    elif sel == 4:
        res = n1 / n2
        if res.is_integer():
            res = int(res)
        print(n1, "/", n2, "=", res)

    elif sel == 5:
        res = n1 ** n2
        if res.is_integer():
            res = int(res)
        print(n1, "^", n2, "=", res)

    elif sel == 6:
        res = n1 % n2
        if res.is_integer():
            res = int(res)
        print("El residuo de", n1, "/", n2, "=", res)

    elif sel == 7:
        res = factorial(num)
        if res.is_integer():
            res = int(res)
        print(num, "factorial =", res)

    elif sel == 8:
        res = sqrt(num)
        if res.is_integer():
            res = int(res)
        print("La raíz de", num, "=", res)

# Termina el programa
print("-- PROGRAM END --")