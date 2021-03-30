from math import sqrt

print("ingrese los valores de la ecuación por favor")

B=float(input("ingrese el valor de B: "))

A=float(input("ingrese el valor de A: "))

C=float(input("ingrese el valor de C: "))

DISCRIMINANTE = ((B**2) - (4*A*C))

print("el discriminante es:", DISCRIMINANTE)

if DISCRIMINANTE >= 0:

  RAIZ1 = ((-B + (sqrt(DISCRIMINANTE)))/(2*A))

  RAIZ2 = ((-B - (sqrt(DISCRIMINANTE)))/(2*A))

  print("la primero raiz es ", RAIZ1)

  print("la segunda raiz es ", RAIZ2)

else:

  print("Raices complejas")