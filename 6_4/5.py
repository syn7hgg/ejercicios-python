n = int(input("ingrese un número para factorial:"))

y = n

z = 1

while y > 1:
    z *= y

    y -= 1

    print("valores al final ciclo de", "n:", n, "y:", y, "z:", z)

print("el resultado del factorial del numero", n, "es", z)
