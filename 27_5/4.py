# UNFINISHED

from random import uniform, randint


def generate_matrix(length, height):
    count1, count2 = 0, 0
    rows = []
    while count2 < height:
        columns = []
        while count1 < length:
            columns.append("{:.2f}".format(uniform(0, 10)))
            count1 += 1
        rows.append(columns)
        count1 = 0
        count2 += 1
    return rows


def print_matrix():
    global length, height, name
    file = open(name + ".txt", "r")
    lines = file.readlines()
    for x in lines:
        i = x.split(" ")
        for j in i:
            print("\t", j, end=" ")


def replace_random():
    global length, height, name
    file = open(name + ".txt", "r")
    lines = file.readlines()
    file.close()
    randrow = randint(0, height)
    randcol = randint(0, length)
    row = lines[randrow]
    columns = row.split(" ")
    columns = [float(x) for x in columns]
    print(columns)
    columns[randcol] = randint(0, 10)
    file = open(name + ".txt", "w")
    lines[randrow] = " ".join(columns).strip() + "\n"
    file.writelines(lines)
    lines = file.readlines()
    return lines


def save_matrix(matrix):
    global length, height, name
    file = open(str(name) + ".txt", "w")
    for x in matrix:  # for each row
        line = ""
        for y in x:
            line += str(y) + " "
        file.write(line + "\n")


length = int(input("ingrese N de la Matriz: "))
height = int(input("ingrese M de la Matriz: "))
name = input("ingrese nombre del archivo: ")
matrix = generate_matrix(length, height)
save_matrix(matrix)
print_matrix()
replace_random()
print_matrix()
