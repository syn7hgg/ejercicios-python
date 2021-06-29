from random import randint

rand = randint(0, 100)

i = int(input())

while i != rand:
    if i < rand:
        print("Es mayor")
    else:
        print("Es menor")

    i = int(input())

print("Correcto")