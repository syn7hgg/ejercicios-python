a = 100
b = 30
c = 20
d = 12
e = 5

while e < a:
    if b % c == 0:
        b = c * d
    else:
        c = b * a
    e += 5

print(a, b, c, d, e)
