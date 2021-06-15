import matplotlib

import pandas

archivo_csv = "NP_csv.csv"


class Persona:

    def __init__(self):

        self.rut = ""

        self.nombre = ""

        self.solemne1 = ""

        self.solemne2 = ""

        self.IBM = ""

        self.tarea1 = ""

        self.tarea2 = ""

        self.hitos = ""

    def setRut(self, rut):

        self.rut = rut

    def setNombre(self, nombre):

        self.nombre = nombre

    def setSolemne1(self, solemne1):

        self.solemne1 = solemne1

    def setSolemne2(self, solemne2):

        self.solemne2 = solemne2

    def setIBM(self, IBM):

        self.IBM = IBM

    def setTarea1(self, tarea1):

        self.tarea1 = tarea1

    def setTarea2(self, tarea2):

        self.tarea2 = tarea2

    def setHitos(self, hitos):

        self.hitos = hitos

    def getRut(self):

        return self.rut

    def getNombre(self):

        return self.nombre

    def getSolemne1(self):

        return self.solemne1

    def getSolemne2(self):

        return self.solemne2

    def getIBM(self):

        return self.IBM

    def getTarea1(self):

        return self.tarea1

    def getTarea2(self):

        return self.tarea2

    def getHitos(self):

        return self.hitos

    def Nota_Presentacion(self, solemne1, solemne2, IBM, tarea1, tarea2, hitos):

        NP1 = 0.2 * float(solemne1) + 0.2 * float(solemne2) + 0.05 * float(IBM) + 0.2 * float(tarea1) + 0.25 * float(
            tarea2) + 0.1 * float(hitos)

        NP = round(NP1, 1)

        return str(NP)

    def Eximidos(self, rut, nombre, solemne1, solemne2, IBM, tarea1, tarea2, hitos):

        NP1 = 0.2 * float(solemne1) + 0.2 * float(solemne2) + 0.05 * float(IBM) + 0.2 * float(tarea1) + 0.25 * float(
            tarea2) + 0.1 * float(hitos)

        NP = round(NP1, 1)

        archivo_a = open("aprobados.txt", "a")

        archivo_e = open("examen.txt", "a")

        if NP >= 5.0:

            archivo_a.write(self.rut + "," + self.nombre + "," + str(NP) + "\n")

        else:

            archivo_e.write(self.rut + "," + self.nombre + "," + str(NP) + "\n")

        archivo_a.close()

        archivo_e.close()

        return print("...Grabación OK...")

    def Eximidos_V2(self):

        archivo_a2 = open("aprobados_v2.txt", "w")

        archivo_e2 = open("examen_v2.txt", "w")

        personas = cargarPersonas()

        for persona in personas:

            NP1 = 0.2 * float(persona.solemne1) + 0.2 * float(persona.solemne2) + 0.05 * float(
                persona.IBM) + 0.2 * float(persona.tarea1) + 0.25 * float(persona.tarea2) + 0.1 * float(persona.hitos)

            NP = round(NP1, 1)

            if NP >= 5.0:

                archivo_a2.write(persona.rut + "," + persona.nombre + "," + str(NP) + "\n")

            else:

                archivo_e2.write(persona.rut + "," + persona.nombre + "," + str(NP) + "\n")

        archivo_a2.close()

        archivo_e2.close()

        return print("...Grabación OK segunda versión...")

    def __str__(self):

        return self.rut + " " + self.nombre + " " + self.solemne1 + " " + self.solemne2 + " " + self.IBM + " " + self.tarea1 + " " + self.tarea2 + " " + self.hitos + " NP=" + self.Nota_Presentacion(
            self.solemne1, self.solemne2, self.IBM, self.tarea1, self.tarea2, self.hitos)


def guardarPersonas(personas):
    personas_f = open("NP.txt", "w")

    for persona in personas:
        personas_f.write(
            str(persona.rut) + "," + str(persona.nombre) + "," + persona.Nota_Presentacion(persona.solemne1,
                                                                                           persona.solemne2,
                                                                                           persona.IBM, persona.tarea1,
                                                                                           persona.tarea2,
                                                                                           persona.hitos) + str("\n"))

    personas_f.close()


def cargarPersonas():
    personas = []

    personas_f = open("estudiantes.txt", "r")

    for persona_l in personas_f:
        datos = persona_l.split(";")

        persona = Persona()

        persona.setRut(datos[0])

        persona.setNombre(datos[1])

        persona.setSolemne1(datos[2])

        persona.setSolemne2(datos[3])

        persona.setIBM(datos[4])

        persona.setTarea1(datos[5])

        persona.setTarea2(datos[6])

        persona.setHitos(datos[7].strip())

        personas.append(persona)

    personas_f.close()

    return personas


personas = cargarPersonas()

guardarPersonas(personas)

for persona in personas:
    print(persona)

    persona.Eximidos(persona.rut, persona.nombre, persona.solemne1, persona.solemne2, persona.IBM, persona.tarea1,
                     persona.tarea2, persona.hitos)

    persona.Eximidos_V2()
