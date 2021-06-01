def get_lines(filename):
    print('Inicio de lectura del archivo', filename + '.')
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def process_lines(lines):
    processed, under, over, processable = [], [], [], []
    for x in lines:
        x = x.strip().split('\t')
        processed.append(x)
    processable = [eval(x[1]) for x in processed]
    avg = sum(processable)/len(processable)
    for x in processed:
        if eval(x[1]) >= avg:
            over.append("%.2f" % eval(x[1]))
        else:
            under.append("%.2f" % eval(x[1]))
    return over, under


def write_file(name, data):
    file = open(name, 'w')
    print('Archivo', name, 'GENERADO')
    for x in data:
        file.write(x + '\n')
    file.close()


filename = 'solo_dolar.txt'
lines = get_lines(filename)
lista_may, lista_men = process_lines(lines)
write_file('dolar_mayor_prom.txt', lista_may)
write_file('dolar_menor_prom.txt', lista_men)
