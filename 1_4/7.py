# UNFINISHED

print("== RUN Parser ==")

i = input("Ingrese su RUT sin dígito verificador: ")

inv = i[::-1]
arr = list(inv)

calc = []
calc.append(int(arr[0]) * 2)
calc.append(int(arr[1]) * 3)
calc.append(int(arr[2]) * 4)
calc.append(int(arr[3]) * 5)
calc.append(int(arr[4]) * 6)
calc.append(int(arr[5]) * 7)
calc.append(int(arr[6]) * 2)
calc.append(int(arr[7]) * 3)

pre1 = calc[0] + calc[1] + calc[2] + calc[3] + calc[4] + calc[5] + calc[6] + calc[7]
pre2 = (pre1 // 11) * 11
pre3 = pre1 - pre2

res = 11 - pre3

print(res)

# Termina el programa
print("-- PROGRAM END --")