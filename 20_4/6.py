numero = int(input("ingresa número: "))
numero = str(numero)
indice = 0
contador = 0
longitud = len(numero)
while indice < longitud:
    contador += int(numero[indice])
    indice += 1
print("La suma de los componentes del número es:", contador)
