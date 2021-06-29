cont = [0, 0, 0, 0] # 0-float, 1-int, 2-pos, 3-neg

i = eval(input())

while i != 0:
    if isinstance(i, float): # podrías utilizar %1 tmb
        cont[0] += 1
    else:
        cont[1] += 1

    if i > 0:
        cont[2] += 1
    elif i < 0:
        cont[3] += 1

    i = eval(input())

print("Decimales:", cont[0])
print("Enteros:", cont[1])
print("Positivos:", cont[2])
print("Negativos:", cont[3])