colores=["azul","morado","rojo","amarillo","lila"]
color=input("Ingresa el color")#Naranja
encontrado=False
for contador in colores:
    print(colores)
    #Si el color es "Rojo", detener el bucle 
    if contador=="Negro":
        print("Color encontrado! Saliendo del bucle")
        encontrado=True
        break 
if not encontrado:
    print("El color,",color, "no se encontro")


