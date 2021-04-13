nombres = ["Maria", "Diego", "RAFAEL"]

deportes = ["tenis", "futbol", "basket"]

frecuencia = ["mucho", "poco", "maomenos"]

i = 0

while i < len(nombres):
    print("{0} juega {1}. {0} practica {2}.".format(nombres[i], deportes[i], frecuencia[i]))

    i = i + 1
