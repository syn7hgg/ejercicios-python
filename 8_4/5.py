print("while con evento")

promedio, total, contar = 0.0, 0, 0

grado = int(input("Introduzca la nota de un estudiante (-1 para salir): "))

while grado != -1:
    total = total + grado

    print("total", total)

    contar = contar + 1

    grado = int(input("Introduzca la nota de un estudiante (-1 para salir): "))

promedio = total / contar

print("Promedio de notas del grado escolar es: " + str(promedio))
