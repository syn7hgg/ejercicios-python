n = int(input('Introduce un número entero entre 1 y 10: '))

m = int(input('Introduce la ubicación M : '))

file_name = 'EJ01-tabla-' + str(n) + '.txt'

try:

    f = open(file_name, 'r')

except FileNotFoundError:

    print('No existe el archivo con la tabla del ', n)

else:

    lines = f.readlines()

    print(lines[m - 1])
