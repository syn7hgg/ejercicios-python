while True:

    orden = input("ingrese operación:")

    if orden == "salir":
        break

    r = eval(orden)

    print("resultado =", r)
