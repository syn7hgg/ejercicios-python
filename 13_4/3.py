print("0: Castellano")

print("1: English")

print("2: Deutsch")

print("3: Francais")

lenguaje = int(input("(0,1,2,3): "))

if lenguaje == 0:

    nombre = input("Cual es tu nombre :")

    print("Hola ", nombre)

elif lenguaje == 1:

    nombre = input("What's your neme? :")

    print("Hello ", nombre)

elif lenguaje == 2:

    nombre = input("Wie heit du :")

    print("Hallo ", nombre)

elif lenguaje == 3:

    nombre = input("Quel est votre nom: ")

    print("Bonjour ", nombre)
