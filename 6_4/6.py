n = int(input("inserta un numero "))

y = n

factorial_total = 1

x = 1

for x in range(n):
    factorial_total *= n

    x += 1

    n -= 1

    print("valor fin ciclo de: ", "n:", n, "x:", x, "range(n):", range(n), "factorial_total:", factorial_total)

print("El factorial de %d es %d" % (y, factorial_total))
