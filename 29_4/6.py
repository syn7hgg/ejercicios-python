def determinante(m):
    d = m[0][0] * m[1][1] - m[0][1] * m[1][0]

    return d


matriz = [[2, 3], [-1, 2]]

d = determinante(matriz)

print("matriz original: ", matriz)

print("determinante: ", d)
