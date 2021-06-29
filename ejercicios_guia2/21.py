i = input()
j = input()
cont, cant = 0, 0

while cont < len(i):
    if i[cont] == j:
        cant += 1
    cont += 1

print(cant)
