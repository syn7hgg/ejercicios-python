n = int(input("ingrese un número para factorial:"))

y = n

z = 1

while y > 1:
    print("valores inicio ciclo de", "n:", n, "y:", y, "z:", z)

    z *= y

    y -= 1

    print("valores al final ciclo de", "n:", n, "y:", y, "z:", z)

print("el resultado del factoria del numero", n, "es", z)
