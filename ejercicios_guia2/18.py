i = int(input())
cont = 0

while cont < 4:
    print("Año", cont, "-", i)
    i = round(i * 1.04, 2)
    cont += 1
