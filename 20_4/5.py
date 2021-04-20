total = 0
num = int(input("Introduzca número (-1 para terminar): "))

while num != -1:
    if num > 0:
        total += num
        num = int(input("Introd un número (-1 para terminar): "))

print("La suma de números ingresados es:", str(total))
num2 = int(input("Ingrese un número: "))
print("El cálculo de la parte entera entre la división total y num2 es:", (total // num2))
print("El cálculo del resto entre total y num2 es:", (total % num2))
