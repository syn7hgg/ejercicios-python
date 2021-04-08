print("while con break")

variable = int(input("ingrese valor: "))

param_break = int(input("ingrese valor break: "))

while variable > 0:

    print('Actual valor de variable:', variable)

    variable = variable - 1

    if variable == param_break:
        break

if param_break > variable:

    print("no hay break!!!!!")

else:

    print("en que parte salio el break.....es en ", param_break)
