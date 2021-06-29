num = int(input())
divs = []
i, j = 1, 0

while i < num and num > 0:
    i += 1
    resid = num%i
    if resid == 0:
        divs.append(i)
        num = num/i
        i = 1

for x in divs:
    print(x)
