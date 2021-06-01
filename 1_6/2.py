def get_lines(filename):
    print('Inicio de lectura del archivo', filename + '.')
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def process_lines(lines):
    processed = []
    for x in lines:
        x = x.strip().split('\t')
        processed.append(x)
    values = [eval(y[1]) for y in processed]
    maximum = max(values)
    for y in processed:
        if eval(y[1]) == maximum:
            return 'Máximo valor del Dólar es: ' + str("%.2f" % maximum) + ' que corresponde a la fecha: ' + y[0]
    return 'NaN'

filename = 'solo_dolar.txt'
lines = get_lines(filename)
print(process_lines(lines))
