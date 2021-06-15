class Coordenada:

    # Se define el constructor, que instancia los distintos objetos

    def __init__(self, _x, _y):
        self.x = _x

        self.y = _y

    def imprimir(self):
        print("El valor de x es: " + str(self.x))

        print("El valor de y es: " + str(self.y))

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def son_iguales(self, c2):
        if self.x == c2.x and self.y == c2.y:
            return True

        return False

    def sumar_Coordenada(self, c2):
        a = self.x + c2.x

        b = self.y + c2.y

        return Coordenada(a, b)


nc1 = Coordenada(4, 8)

nc2 = Coordenada(3, 7)

print("imprimir nc1 y nc2")

r = nc1.imprimir()

print("segunda coordenada")

r = nc2.imprimir()

print("imprimir nc2 (3,7) ")

print(nc2)

print("son iguales nc2 (3,7) ")

r = nc1.son_iguales(nc2)

print(r)

print("sumar nc1(4,8) y nc2 (3,7) ")

r = nc1.sumar_Coordenada(nc2)

print(r)
