f = 10


def factorial(n):
    f = 1

    i = 1

    while i <= n:
        f = f * i

        i = i + 1

    return f


print("El factorial de ", f, " es ", factorial(f))
