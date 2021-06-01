def get_lines(filename):
    print('Inicio de lectura del archivo', filename + '.')
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def process_lines(lines):
    processed = []
    for x in lines:
        x = x.strip().split('\t')
        processed.append(eval(x[1]))
    print(processed)
    avg = sum(processed)/len(processed)
    return avg

filename = 'solo_dolar.txt'
lines = get_lines(filename)
print("El promedio del Dólar es %.2f" % process_lines(lines))
