print("== Vocal o consonante? ==")

v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

sel = input("Ingrese una modalidad (ascii o lista): ")

if sel != "ascii":
    i = input("Ingrese una letra: ")

    if i in v:
        print("Es una vocal.")
    else:
        print("Es una consonante o un número.")
else:
    char = input("Ingrese una letra: ")
    parsed = ord(char)

    if parsed == 65 or parsed == 69 or parsed == 73 or parsed == 79 or parsed == 85:
        print("Es una vocal mayúscula.")
    elif parsed == 97 or parsed == 101 or parsed == 105 or parsed == 111 or parsed == 117:
        print("Es una vocal minúscula.")
    else:
        print("Es una consonante o un número.")

# Termina el programa
print("-- PROGRAM END --")
