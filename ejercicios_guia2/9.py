orig = input("Cree una contraseña: ")
p = input("Ingrese la contraseña: ")
cont = 0

while p != orig and cont < 2:
    cont += 1
    p = input("Incorrecto, intente de nuevo: ")

if p == orig:
    print("Correcto")
else:
    print("Error, hasta luego")