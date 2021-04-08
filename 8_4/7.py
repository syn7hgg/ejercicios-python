import random

from random import randint

print("random choice")

frutas = ["cerezas", "limones", "sandias", "peras", "manzanas", "higos", "Duraznos", "damascos", "plátanos", "ciruelas"]

for i in range(5):
    print(random.choice(frutas))

print("random shuffle")

sacar_numero = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

for i in range(3):
    random.shuffle(sacar_numero)

    print(sacar_numero)
