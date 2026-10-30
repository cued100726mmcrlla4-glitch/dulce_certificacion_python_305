lista_super=[]
cantidad=int(input("¿cuantos productos quieres agregar al carrito?"))
for contador in range(cantidad):
    producto=input("Ingresa el producto" ,contador+1)
    carrito.append(producto)
print("\nTu lista de compras es:")
print(carrito)

