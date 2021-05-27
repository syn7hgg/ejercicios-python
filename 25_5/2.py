from random import randint


def generate_matrix(length):
    count1, count2 = 0, 0
    rows = []
    while count2 < length:
        columns = []
        while count1 < length:
            columns.append(randint(0, 10))
            count1 += 1
        rows.append(columns)
        count1 = 0
        count2 += 1
    return rows


def print_matrix():
    global length
    file = open("matriz_" + str(length) + "_por_" + str(length) + ".txt", "r")
    lines = file.readlines()
    for x in lines:
        print(x, end="")


def save_matrix(matrix):
    global length
    file = open("matriz_" + str(length) + "_por_" + str(length) + ".txt", "w")
    for x in matrix:  # for each row
        line = ""
        for y in x:
            if len(str(y)) == 1:
                line += str(y) + "   "
            else:
                line += str(y) + "  "
        file.write(line + "\n")


length = int(input("ingrese N de la Matriz: "))
matrix = generate_matrix(length)
save_matrix(matrix)
print_matrix()
