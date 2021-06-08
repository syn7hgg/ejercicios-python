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


pl = Persona()

pl.setRut("12334768-8")

pl.setNombre("Juan López")

print(pl)
