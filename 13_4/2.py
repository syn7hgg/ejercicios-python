print("--------------")

print("string inicial")

saludo="amiga"

print(saludo)

print(saludo[4])

print("--------------")

print("convertir a lista")

saludo_l=list(saludo)

print(saludo_l)

saludo_l[4]='o'

print(saludo_l)

print("--------------")

print("metodo join")

saludo="".join(saludo_l)

print(saludo)