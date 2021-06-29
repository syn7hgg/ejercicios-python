from math import *


def es_primo(i):
    iter = 1
    while iter < i:
        res = i % iter
        if res == 0 and i != 1:
            if i % 2 == 0 and i != 2 or i % 3 == 0 and i != 3 or i % 5 == 0 and i != 5:
                return False
            elif isinstance(sqrt(i), int):
                return False
        else:
            return True

        iter += 1
    return False

num = int(input())

if es_primo(num) or num == 2:
    print("Sí.")
else:
    print("No.")
