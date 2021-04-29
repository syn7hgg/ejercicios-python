from numpy import matrix
from numpy.linalg import *

# se puede crear una matriz con una lista

matriz = matrix([[2, 3], [-1, 2]])

print(det(matriz))

# también se puede crear una matriz con strings

matriz = matrix("2,3;-1,2")

print(det(matriz))
