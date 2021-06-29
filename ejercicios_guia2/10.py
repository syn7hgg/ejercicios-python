i = int(input())
list = [int(x) for x in str(i)]
cont = 0

for x in list:
    if x == 1:
        cont += 1

print(cont)
