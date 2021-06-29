from random import randint


def generate_data(city_count):
    gen = []
    c1 = 0
    while c1 < city_count:
        pre = []
        c2 = 0
        while c2 < 7:
            pre.append(randint(200, 1000))
            c2 += 1
        gen.append(pre)
        c1 += 1

    print("===== DATA GENERADA ===== ")
    count = 0
    for x in gen:
        print("Comuna", str(count) + ":", x)
        count += 1

    return gen


def calculate_data(data):
    count = 0
    c1, c2 = 0, 0
    avgs, avgdays = [], []
    maxavg, minavg = [], []
    for x in data:
        avg = sum(x)/len(x)
        avgs.append(round(avg))

    maxsingle = max(avgs, key=float)
    minsingle = min(avgs, key=float)

    for x in [i for i, n in enumerate(avgs) if n == maxsingle]:
        maxavg.append([[i for i, n in enumerate(avgs) if n == maxsingle][c1], maxsingle])
        c1 += 1
    for x in [i for i, n in enumerate(avgs) if n == minsingle]:
        minavg.append([[i for i, n in enumerate(avgs) if n == minsingle][c2], minsingle])
        c2 += 1

    count = 0
    while count < 7:
        pre = 0
        for x in data:
            pre += x[count]
        avgdays.append(round(pre/len(data)))
        count += 1

    avgsum = 0
    for x in data:
        avgsum += sum(x)
    totalavg = round(avgsum/len(data*7))

    return avgs, maxavg, minavg, avgdays, totalavg


def use_data(avgs, maxavg, minavg, avgdays, totalavg):
    file = open('dashboardBasuraRecolectada.txt', 'w')
    c1 = 0

    # All averages
    file.write("===== PROMEDIOS POR COMUNA =====\n")
    print("===== PROMEDIOS POR COMUNA =====")
    for x in avgs:
        line = "Comuna " + str(c1) + ": " + str(x) + " bolsas por día\n"
        file.write(line)
        print(line.strip())
        c1 += 1

    # Max averages
    c1, c2 = 0, 0
    for x in maxavg:
        c1 += 1
    for x in minavg:
        c2 += 1

    if c1 == 1:
        line = "===== MÁXIMO PROMEDIO =====\n"
    else:
        line = "===== MÁXIMOS PROMEDIOS =====\n"
    file.write(line)
    print(line.strip())
    for x in maxavg:
        line = "Comuna " + str(x[0]) + ": " + str(x[1]) + " bolsas por día\n"
        file.write(line)
        print(line.strip())

    # Min averages
    if c2 == 1:
        line = "===== MÍNIMO PROMEDIO =====\n"
    else:
        line = "===== MÍNIMOS PROMEDIOS =====\n"
    file.write(line)
    print(line.strip())
    for x in minavg:
        line = "Comuna " + str(x[0]) + ": " + str(x[1]) + " bolsas por día\n"
        file.write(line)
        print(line.strip())

    # Average per day
    line = "===== PROMEDIO POR DÍA =====\n"
    file.write(line)
    print(line.strip())
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    count = 0
    for x in avgdays:
        line = str(days[count]) + " (" + str(count) + "): " + str(x) + " bolsas\n"
        file.write(line)
        print(line.strip())
        count += 1

    # General average
    line = "===== PROMEDIO GENERAL =====\n"
    file.write(line)
    print(line.strip())
    line = "Promedio: " + str(totalavg) + " bolsas por día\n"
    file.write(line)
    print(line.strip())

    file.write("\n")
    print()
    file.write("===== FIN DE LOS DATOS =====\n")
    print("===== FIN DE LOS DATOS =====")


data = generate_data(52)
comunaAvgs, comunaMax, comunaMin, comunaAvgDays, comunaTotal = calculate_data(data)
use_data(comunaAvgs, comunaMax, comunaMin, comunaAvgDays, comunaTotal)
