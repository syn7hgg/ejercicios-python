age = int(input())
sal = int(input())
ant = int(input())

if age >= 18 and sal >= 400000 and ant >= 36:
    print("Crédito aprobado.")
else:
    if age < 18:
        print("Edad insuficiente.")
    if sal < 400000:
        print("Sueldo insuficiente.")
    if ant < 36:
        print("Antiguedad insuficiente.")
