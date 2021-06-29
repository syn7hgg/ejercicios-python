cont1, cont2 = 0, 0
graSum, code, yea, mon, day, qua, jum = 0, 0, 0, 0, 0, 0, 0
gra, li = [], []
sea = ""

try:
    code = int(input("Ingrese el código de la competencia: "))
except ValueError:
    print("El código debe contener únicamente dígitos numéricos.")
    quit()
code = str(code)

if len(code) < 12 or len(code) > 35:
    print("Código incorrecto. Rango aceptable: [12,35].\nSe recibió un largo de:", len(code))
    quit()

# Example: 1956052134777766665555

try:
    yea = int(code[0:4])
    mon = int(code[4:6])
    day = int(code[6:8])
    qua = int(code[8])
    jum = int(code[9])

    li = code[10:(10 + int(qua) * int(jum))]
    li = [str(x) for x in li]
except IndexError:
    print("El código parece estar mal ingresado.\nAsegúrate de haber escrito todos los dígitos necesarios.")
    quit()

if qua < 2 or qua > 5 or jum < 1 or jum > 5:
    print("Valores incorrectos. Se aceptan los siguientes rangos:")
    print("Competidores: [2,5]\nSaltos: [1,5]")
    print("Se recibió:\nCompetidores:", qua, "\nSaltos:", jum)
    quit()

while cont2 < (int(jum) * int(qua)):
    try:
        while cont1 < int(jum):
            if int(li[cont2]) < 1 or int(li[cont2]) > 7:
                print("Puntaje incorrecto: El puntaje no debe ser menor que uno ni mayor que 7.")
                quit()
            graSum += int(li[cont2])
            cont1 += 1
            cont2 += 1
        gra.append((graSum / int(jum)))
        cont1 = 0
        graSum = 0
    except IndexError:
        print("El código parece estar mal ingresado.\nAsegúrate de haber escrito todos los dígitos necesarios.")
        quit()

win = gra.index(max(gra)) + 1

if (day >= 21 and mon == 10) or (mon == 11) or (mon == 12) or (mon <= 4) or (day < 21 and mon == 5):
    sea = "Verano"
else:
    sea = "Invierno"

# RESULTS
print("Año:", str(yea))
print("Temporada:", sea)
print("Cantidad de competidores:", str(qua))
print("Cantidad de clavados:", str(jum))
print("Competidor ganador:", win)
print("Promedio", str(gra[(win - 1)]))
