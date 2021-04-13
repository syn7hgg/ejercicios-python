nombres = ["Maria", "Diego"]

deportes = ["tenis", "futbol"]

frecuencia = ["mucho", "poco"]

i = 0

while i < len(nombres):
    print("{0} juega {1}. {0} practica {2}.".format(nombres[i], deportes[i], frecuencia[i]))

    i = i + 1
