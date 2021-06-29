n = 10
a = 20
b = 0
z = 30

print("A: ", end="")
if n > 0:
    if a > b:
        z = a
    else:
        z = b
print(z, end="\n")

n = 10
a = 20
b = 0
z = 30

print("B: ", end="")
if n > 0:
    if a > b:
        z = a
else:
    z = b
print(z, end="\n")