import numpy as np
from random import uniform, choice

arrList = []
lista_matriz = ["array1", "array2", "array3"]


def generate_number_array(size):
    count = 0
    a = np.empty(0)
    while count < size:
        a = np.append(a, [[uniform(0, 1)]])
        count += 1

    return a


def append_to_list(arr):
    global arrList
    arrList.append(arr.tolist())


def save_to_file(name, data):
    file = open(name+".txt", "a")
    for x in data:
        # print(x)
        file.write(str(x) + "\n")
    file.close()


def read_file(name):
    print("Leyendo archivo " + name + ".txt")
    file = open(name+".txt", "r")
    print("Finalizada la lectura de " + name + ".txt")
    return file.read()


def main():
    global arrList
    n = int(input("Ingrese N: "))
    m = int(input("Ingrese M: "))
    count = 0

    while count < m:
        append_to_list(generate_number_array(n))
        count += 1

    save_to_file(choice(lista_matriz), arrList)
    print(read_file(choice(lista_matriz)))


main()