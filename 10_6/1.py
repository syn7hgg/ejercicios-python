class Fraccion:

    def __init__(self, n, d):
        self.numerador = n

        self.denominador = d


n = int(input("Ingrese Numerador: "))

d = int(input("Ingrese Denominador: "))

f = Fraccion(n, d)

print(f.numerador)

print(f.denominador)
