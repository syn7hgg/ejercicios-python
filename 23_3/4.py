"Sorter by Andrés c:"

num = [0, 0, 0]

num[0] = float(eval(input("Ingrese el primer número: ")))
num[1] = float(eval(input("Ingrese el segundo número: ")))
num[2] = float(eval(input("Ingrese el tercer número: ")))

ordenados = sorted(num, reverse=True)

print(ordenados[0])
print(ordenados[1])
print(ordenados[2])
