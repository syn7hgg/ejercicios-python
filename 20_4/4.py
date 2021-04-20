a = 100
b = 30
c = 20
d = 12
e = 5

while e < a:
    while e < a:
        if b % c == 0:
            b = c * d
        else:
            c = b * a
            d = c * b
        e += 5
    e += 20
    b *= b

print(a, b, c, d, e)
