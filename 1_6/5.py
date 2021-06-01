def get_lines(filename):
    print('Inicio de lectura del archivo', filename + '.')
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def process_lines(lines):
    processed = []
    for x in lines:
        x = x.strip().split('\t')
        processed.append("%.2f" % eval(x[1]))
    sorted_values = sorted(processed, reverse=True)
    string_final = ""
    for x in sorted_values:
        string_final += str(x)+","
    string_final = string_final[:-1]
    return string_final


def write_file(name, data):
    file = open(name, 'w')
    print('Archivo', name, 'GENERADO')
    file.write(data)
    file.close()


filename = 'dolar_mayor_prom.txt'
lines = get_lines(filename)
ordered = process_lines(lines)
write_file('dolar_mayor_prom_ordmayor.txt', ordered)
filename = 'dolar_menor_prom.txt'
lines = get_lines(filename)
ordered = process_lines(lines)
write_file('dolar_menor_prom_ordmayor.txt', ordered)
