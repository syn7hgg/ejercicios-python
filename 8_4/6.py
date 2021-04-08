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

import random

from random import randint

print("Random float con 2 decimal")

num2 = round(random.random(), 2)

print(num2)

num2 = round(random.uniform(33.33, 66.66), 2)

print(num2)

print("Random float con un 1 decimal")

print(round(random.random(), 1))

print(round(random.uniform(33.33, 66.66), 1))
