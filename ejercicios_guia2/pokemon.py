ataca = "electric"

defiende = "water"


def Tabla_Efectividad(ataca, defiende):
    datos = open("tabla_efectividad.csv", "r")

    linea = datos.readline()

    linea = linea.strip()

    indice = linea.split(",").index(defiende)

    while linea:

        linea = datos.readline()

        linea_s = linea.split(",")

        if linea_s[0] == ataca:
            return float(linea_s[indice])


def Obtener_Data(pokemon):
    datos = open("pokemon_data.csv", "r")

    contador = 2

    for linea in datos:

        poke_data = linea.split(",")

        if (pokemon == poke_data[0]):
            pokemon_nombre = poke_data[0]

            tipo = poke_data[1]

            puntos_de_vida = int(poke_data[2])

            puntos_de_ataque_fisico_base = int(poke_data[3])

            puntos_de_defensa_fisica_base = int(poke_data[4])

            puntos_de_ataque_especial_base = int(poke_data[5])

            puntos_de_defensa_especial_base = int(poke_data[6])

            puntos_de_velocidad_base = int(poke_data[7])

            nro = contador

            ataques = poke_data[8].split(";")

            return pokemon_nombre, tipo, puntos_de_vida, puntos_de_ataque_fisico_base, puntos_de_defensa_fisica_base, puntos_de_ataque_especial_base, puntos_de_defensa_especial_base, puntos_de_velocidad_base, nro, ataques

        contador = contador + 1


print(Obtener_Data(pokemon))

print(Tabla_Efectividad(ataca, defiende))
