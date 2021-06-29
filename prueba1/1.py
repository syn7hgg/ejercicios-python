aux = int(input())
real = aux
inv = 0

while aux > 0:
    reserva = aux % 10
    print("Reserva:", reserva)
    inv = inv * 10 + reserva
    print("Inv:", inv)
    aux //= 10
    print("Aux:", aux)
if inv == real:
    print("Es capicúa")
else:
    print("No es capicúa")
