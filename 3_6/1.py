def get_lines(filename):
    print('Inicio de lectura del archivo', filename + '.')
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def process_lines(lines):
    processed = []
    for x in lines:
        x = x.split('\t')
        processed.append(x)
    return processed


def search_data(mon, day, data, reverse):
    if reverse:
        processed = []
        for x in data:
            sep = x[0].strip().split('-')
            if sep[0] == day and sep[1] == mon:
                continue
            else:
                processed.append(x)
        generate_file('meses-resto.txt', processed)
        return True
    else:
        for x in data:
            sep = x[0].strip().split('-')
            if int(sep[0]) == day and sep[1] == mon:
                generate_file(str(mon) + '-' + str(day) + '.txt', [x])
                return True
    return False


def generate_file(name, data):
    file = open(name, 'w')
    for x in data:
        file.write(x[0].strip() + "#" + x[1].strip() + "\n")
    file.close()
    return True


month = input("Ingrese mes: ")
day = int(input("Ingrese día: "))
data = get_lines('solo_dolar.txt')
proc = process_lines(data)
search_data(month, day, proc, False)
search_data(month, day, proc, True)