i = int(input())
j = int(input())
cont = 1
res = 0

# será i/j

while j*cont < i:
    cont += 1

print(i - (j*(cont-1)))

print("Compr: ", str(i%j))