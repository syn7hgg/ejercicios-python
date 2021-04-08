n = int(input("ingrese n: "))

while n < 10:

    n += 1

    print("n es : ", n)

    if n == 8:
        print("es el continue")

        continue

    print(n, end="  ")
