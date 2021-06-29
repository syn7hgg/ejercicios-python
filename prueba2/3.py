def grabarResultados(productoL, precioL, productoH, precioH, media, archivo="vendidos.txt", modo="w"):
    salida = open(archivo, modo)
    salida.write("La media de los precios es:"+str(media)+"\n")
    salida.write("El precio minimo es :"+str(precioL)+" Corresponde a:"+productoL+"\n")
    salida.write("El precio maximo es :"+str(precioH)+" Corresponde a:"+productoH+"\n")
    salida.close()


grabarResultados("Azucar",1200,"Leche",800,1000,"resultados.txt")
grabarResultados("Sal",600,"Leche",800,700)
grabarResultados("Azucar",1200,"Arroz",1300,1250,"vendidos.txt","a")