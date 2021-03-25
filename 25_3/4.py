pt = float(input("Ingrese el PT: "))
pi = float(input("Ingrese el PI: "))
ne = float(input("Ingrese la nota de examen: "))
pp = float(input("Ingrese la nota de presentación: "))

res = pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1
res = round(res, 1)

print("Tu promedio ponderado es", res)