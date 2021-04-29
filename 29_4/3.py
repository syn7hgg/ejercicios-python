l = [1, 2, 3, 4, 5, 6, 7, 8]

longitud = len(l)

print("el valor de len(1)", len(l))

print("---------------------------")

print("La longitud de la lista es: ", longitud)

print("El último elemento de la lista es: ", l[longitud - 1])

print("version2 El último elemento de la lista es: ", l[-1])

print("los números pares: ", l[1::2])

print("los números Impares: ", l[::2])

print("los elementos al centro son: ", l[3:5])

for n in l:
    i = l.index(n)

    print("l[%d]" % i, n, sep=" ", end=" : ")
