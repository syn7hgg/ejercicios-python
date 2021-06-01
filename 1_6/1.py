def get_lines(filename):
    print('Inicio de lectura del archivo', filename + '.')
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def process_lines(lines):
    processed = []
    for x in lines:
        x = x.split('\t')
        processed.append("Para la fecha: " + x[0] + " el valor del dólar es: " + x[1])
    return processed


filename = 'solo_dolar.txt'
lines = get_lines(filename)
proc = process_lines(lines)
for y in proc:
    print(y)
print('Fin de lectura del archivo', filename + '.')
