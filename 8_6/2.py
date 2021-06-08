class Persona:

    def __init__(self):
        self.rut = ""

        self.nombre = ""

    def setRut(self, rut):
        self.rut = rut

    def setNombre(self, nombre):
        self.nombre = nombre

    def getRut(self):
        return self.rut

    def getNombre(self):
        return self.nombre

    def __str__(self):
        return self.rut + " " + self.nombre


# pl=Persona()

# pl.setRut("12334768-8")

# pl.setNombre("Juan López")

# print(pl)


def guardarPersonas(personas):
    personas_f = open("personas2.txt", "w")

    for persona in personas:
        personas_f.write(str(persona) + "\n")

    personas_f.close()


def cargarPersonas():
    personas = []

    personas_f = open("personas.txt", "r")

    for persona_l in personas_f:
        datos = persona_l.split(",")

        persona = Persona()

        persona.setRut(datos[0])

        persona.setNombre(datos[1].strip())

        personas.append(persona)

    personas_f.close()

    return personas


personas = cargarPersonas()

for persona in personas:
    print(persona)

guardarPersonas(personas)
