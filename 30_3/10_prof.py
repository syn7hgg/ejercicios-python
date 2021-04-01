mes=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

m=int(input("ingresa un numero : "))

if(m >= 1 and m <= 12):

    print("el mes " + str(m) + " es : " + mes[m - 1])

else:

    print("No es un mes existente")