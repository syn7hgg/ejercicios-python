PI = 3.1415926535

print("--- FAVOR INGRESE LAS UNIDADES EN CM ---")

L = float(input("Ingrese el largo: "))

A = float(input("Ingrese el Ancho: "))

H = float(input("Ingrese el Altura: "))

print("el volumen es: ", L*A*H)

R = float(input("Ingrese el Radio: "))

print("su perimetro es: ", 2*PI*R)

print("su perimetro redondeado a 2 cifras es: ", round(2*PI*R,2))

print("su area es: ", PI*R*R)

print("su area redondeado a 2 cifras es: ", round(PI*R*R,2))