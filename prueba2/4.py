import random
jugo = ["naranja", "limon", "piña", "frutilla", "granadina", "sandia", "melón", "durazno", "damasco"]
entrada = ["lechuga", "palmito", "chilena", "choclo", "cebolla", "repollo", "palitos de ajo"]
plato_fondo = ["pure pollo", "palta reina", "lomo a lo pobre", "asado aleman", "caldillo de congrio", "mariscal", "fideos con salsa"]
dia = ["lunes", "martes", "miércoles", "jueves", "viernes"]
nombre = "casino"
arch = open(nombre+'.txt','w')
d = 0
while d<len(dia):
    j = random.choice(jugo)
    e = random.choice(entrada)
    pf=random.choice(plato_fondo)
    linea="Para el dia "+dia[d]+"==>"+" el jugo es "+j+", la entrada es: "+e+" y el plato de fondo es: "+pf+"\n"
    arch.write(linea)
    d += 1
arch.close()
print("*************************************************")
print("lectura del archivo %s del Menú de la semana" % (nombre))
print()
archivo = open(nombre+'.txt','r')
B=archivo.readlines()
for i in range(len(B)):
    for k in range(len(B[i])):
        print(B[i][k],end="")
print()