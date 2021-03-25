# ENTRADA

Nombre = str(input("ingresa tu Nombre: "))

#Cantidad de mallas de naranjas que UD. compró

Cantidad_de_Mallas = int(input("Ingrese la cantidad de mallas de Naranjas que compró: "))

#Cantidad de naranjas que vienen en una malla de naranjas

Naranjas_Por_Malla = int(input("Ingrese la cantidad de naranjas por malla: "))

#Cantidad de naranjas por vaso

Naranjas_Por_Vaso = int(input("Ingrese la cantidad de naranjas por vaso de jugo: "))

#Cantidad de familiares a los que se les dio un vaso de jugo

Cantidad_Familiares = int(input("Ingrese la cantidad de Familiares que le preparo un vaso de jugo: "))



# PROCESAMIENTO

# Calcular el total de naranjas 

Naranjas_Totales = Cantidad_de_Mallas * Naranjas_Por_Malla

# Calcular las naranjas gastados en los vasos de jugo

Naranjas_Utilizados_Vasos = Naranjas_Por_Vaso * Cantidad_Familiares

# Calcular las naranjas que van a quedar

Naranjas_Restantes = Naranjas_Totales - Naranjas_Utilizados_Vasos



# SALIDA

# se especifica que muestre su nombre y las naranjas que sobran

print("Estimada(o)", Nombre, "te quedan", Naranjas_Restantes, "naranjas")
