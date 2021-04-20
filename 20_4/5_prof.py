total = 0

num = int(input("Introduzca némro (-1 para terminar de sumar): "))

while num != -1:

    if num > 0:
        total += num

        num = int(input("Introduzca número (-1 para terminar de sumar): "))

print("La suma de números ingresado es: " + str(total))

num2 = int(input("ingrese un número: "))

print("El cálculo de la parte entre la división total y num2 es:", total // num2)

print("El cálculo del resto entre total y num2 es:", total % num2)
