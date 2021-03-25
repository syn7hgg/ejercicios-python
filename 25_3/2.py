name = input("Ingrese su nombre: ")
bask = int(eval(input("Ingrese el número de mallas: ")))
x = int(eval(input("Ingrese el número de naranjas por malla: ")))
y = int(eval(input("Ingrese el número de naranjas requeridas por vaso: ")))
n = int(eval(input("Ingrese el número de integrantes de la familia: ")))
# z = nro de naranjas sobrantes

tot = x * bask
print("Naranjas totales: ", tot)

z = tot - n*y

print("A", name, "le sobrarán", z, "naranjas")
