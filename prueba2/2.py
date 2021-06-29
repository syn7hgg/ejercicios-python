def inicializarAsientos(airbus, asientos, hileras):
    i = 0
    while i < asientos:
        f = ["_"] * hileras
        airbus.append(f)
        i += 1
    return airbus


avión = []
print(inicializarAsientos(avión, 3, 2))