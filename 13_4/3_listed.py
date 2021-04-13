preguntas = [

    "Cual es tu nombre :",

    "What's your neme? :",

    "Wie heit du :",

    "Quel est votre nom: "

]

saludos = [

    "Hola %s !",

    "Hello %s !",

    "Hallo %s !",

    "Bonjour %s !"

]

print("0: Castellano")

print("1: English")

print("2: Deutsch")

print("3: Francais")

lenguaje = int(input("(0,1,2,3): "))

nombre = input(preguntas[lenguaje])

print(saludos[lenguaje] % nombre)
