print("== Ordenador ==")

i = eval(input("Ingrese el primer número: "))
j = eval(input("Ingrese el segundo número: "))
k = eval(input("Ingrese el tercer número: "))

if i > j:
    if i > k:
        if j > k:
            print(i, j, k)
        else:
            print(i, k, j)
    else:
        print(k, i, j)
else:
    if j > k:
        if k > i:
            print(j, k, i)
        else:
            print(j, i, k)
    else:
        print(k, j, i)

# Termina el programa
print("-- PROGRAM END --")