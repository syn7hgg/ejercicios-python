Edad = int(input("ingrese edad: "))

Sueldo_liquido = int(input("ingres su sueldo liquido: "))

Antiguedad = int(input("ingrese antiguedad en meses: "))

Antiguedad_a = Antiguedad // 12

if (Edad >= 18) and (Sueldo_liquido >= 400000) and (Antiguedad_a >= 3):

    print("crédito de consumo aprobado")

elif Edad < 18 and Sueldo_liquido < 400000 and Antiguedad_a < 3:

    print("NO CUMPLE CON NINGUN REQUISITO")

elif Edad < 18 and Sueldo_liquido < 400000:

    print("No cumple con la Edad y con el sueldo liquido")

elif Edad < 18 and Antiguedad_a < 3:

    print("No cumple con la Edad y con la antiguedad")

elif Sueldo_liquido < 400000 and Antiguedad_a < 3:

    print("No cumple con el sueldo liquido y con la antiguedad")

elif Edad < 18:

    print("Ud. no es mayor de edad")

elif Sueldo_liquido < 400000:

    print("sueldo liquido insuficiente")

elif Antiguedad_a < 3:

    print("no cumple con la cantidad de años de antiguedad")
