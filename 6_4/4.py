while True:

    orden = input("ingrese operación:")

    if orden == "clear":
        print("borar memoria........")

        continue

    print("-------------------------")

    r = eval(orden)

    print("resultado =", r)
