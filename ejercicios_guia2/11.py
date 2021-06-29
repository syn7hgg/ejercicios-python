from random import randint

rand = randint(100, 9999)
print(rand)
i = int(input())
listRand = [int(x) for x in str(rand)]
cont = 0

for x in listRand:
    if i == x:
        cont += 1

if cont > 0:
    print("Aparece")
else:
    print("No aparece")