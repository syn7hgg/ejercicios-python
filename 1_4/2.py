print("== Ordenador (Mod) ==")

i = eval(input("Ingrese el primer número: "))
j = eval(input("Ingrese el segundo número: "))
k = eval(input("Ingrese el tercer número: "))

# CASOS SIN IGUALDAD
if i != j and j != k and i != k:
    if i > j:
        if i > k:
            if j > k:
                print(i,)
                print(j)
                print(k)
            else:
                print(i)
                print(k)
                print(j)
        else:
            print(k)
            print(i)
            print(j)
    else:
        if j > k:
            if k > i:
                print(j)
                print(k)
                print(i)
            else:
                print(j)
                print(i)
                print(k)
        else:
            print(k)
            print(j)
            print(i)
# CASOS DE IGUALDAD O SEMI-IGUALDAD
else:
    if i == j and i == k:
        print(i, j, k)
    if i == j and i != k:
        print(k)
        print(i, j)
    if i == k and i != j:
        print(j)
        print(i, k)
    if i != k and j == k:
        print(i)
        print(j, k)

# Termina el programa
print("-- PROGRAM END --")