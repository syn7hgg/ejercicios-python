import math

print("Ingrese los valores de la ecuación, por favor.")

B=float(input("Ingrese el valor de B: "))

A=float(input("Ingrese el valor de A: "))

C=float(input("Ingrese el valor de C: "))

DISCRIMINANTE = ((B**2) - (4*A*C))

print("El discriminante es:", DISCRIMINANTE)

if DISCRIMINANTE >= 0:

  RAIZ1 = ((-B + (math.sqrt(DISCRIMINANTE)))/(2*A))

  RAIZ2 = ((-B - (math.sqrt(DISCRIMINANTE)))/(2*A))

  print("La primera raíz es ", RAIZ1)

  print("La segunda raíz es ", RAIZ2)

else:

  print("Raíces complejas")