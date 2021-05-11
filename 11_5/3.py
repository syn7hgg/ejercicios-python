def es_primo(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


while True:
    try:
        num = int(input("Ingrese número (0 para salir): "))
        if num == 0:
            break
        res = es_primo(num)
        if res:
            print("Es primo.")
        else:
            print("No es primo.")
    except ValueError:
        print("Debe ser entero: ")
