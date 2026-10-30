#Creando un ciccionario en python
persona={
    "nombre":"sofia",
    "edad":28,
    "profesion":"Ingenieria",
    "estudiante":False 
}
print(persona)
#Accediendo a un valor especifico 
print(persona["profesion"])
#Se puede utilizar el metodo.get()
#Es util que no da error si la clave no existe 
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciudad"]="San pepe ranch"
print(persona)
#Recorrer un diccionario con un bucle
for clave,valor in persona.items():
    print(f"(clave),(valor)")
    