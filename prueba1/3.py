p1 = input()
p2 = input()

r = True
largo = len(p1)
if largo != len(p2):
    r = False
else:
    cont = 0
    while cont < largo:
        if p1[cont] != p2[largo - (cont + 1)]:
            r = False
        cont = cont+1

print(r)
