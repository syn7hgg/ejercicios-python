def parse_file(name):
    parsed = []
    file = open(name, 'r')
    data = file.readlines()
    file.close()
    for x in data:
        sep = x.strip().split(';')
        parsed.append(sep)
    return parsed


def calculate_sp(data):
    count = 0
    pre, final = [], []
    for x in data: # Bidimensional list, contains lists with satisfaction indexes and company info
        try:
            final.append([x[0], x[1]])
            sp = ((.25 * eval(x[2])) + (.25 * eval(x[3])) + (.3 * eval(x[4])) + (.1 * eval(x[5])) + (.1 * eval(x[6])))
            sp = round(sp, 2)
            pre.append(sp)
        except ValueError:
            print("Parece haber un error con el tipo de datos. Omitiendo esta ocurrencia.")
            pass
    while count < len(final):
        final[count].append(pre[count])
        count += 1
    return final


def sort_sp(data):
    file1 = open('SPE_Reprobados_CIATel.txt', 'w')
    file2 = open('SPE_Aprobados_CIATel.txt', 'w')
    for x in data:
        try:
            if float(x[2]) <= 3:
                file1.write(x[0] + ';' + x[1] + ';' + str(x[2]) + '\n')
            elif float(x[2]) > 4:
                file2.write(x[0] + ';' + x[1] + ';' + str(x[2]) + '\n')
        except ValueError:
            print("Parece haber un error con el tipo de datos. Omitiendo esta ocurrencia.")
            pass
    file1.close()
    file2.close()
    return True


data = parse_file('SatisfaccionServiciosTelefonía.txt')
calc = calculate_sp(data)
if sort_sp(calc):
    print("Procesamiento terminado. Archivo generado correctamente.")
