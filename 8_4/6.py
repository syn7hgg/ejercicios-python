import random

from random import randint

print("Random entero")

i = 2

j = 10

m = random.randint(i, j)

print(m)

print("Random entero")

i = 1000

j = 10000

m = random.randint(i, j)

print(m)

print("Random numeros enteros con rango")

print(random.randrange(5, 27, 4))

print("Randon de Enteros dado un rango en una lista")

z = [randint(1, 20) for _ in range(60)]

print(z)
