# Calculadora M.C.D (Unfinished)

def calculate_dividers(num1, num2):
    div1, div2 = [], []
    count = 1
    while count < num1:
        if num1 % count == 0:
            div1.append(count)
        count += 1
    count = 1
    while count < num2:
        if num2 % count == 0:
            div2.append(count)
        count += 1
    return div1, div2


def verify_dividers(num1, num2, div1, div2):
    verified = []
    for x in div1:
        if num2 % x == 0:
            verified.append(x)
    for y in div2:
        if num1 % y == 0:
            verified.append(y)
    return max(verified)


num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
res1, res2 = calculate_dividers(num1, num2)
mcd = verify_dividers(num1, num2, res1, res2)

print("El MCD de", str(num1), "y", str(num2), "es:", mcd)