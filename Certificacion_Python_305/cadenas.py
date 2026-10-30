#Cadenas y concentracion con(+)
Cadena1='Hola'
Cadena2="Mundo"
multilinea="""Esto es una cadena 
de varias lineas"""
print(Cadena1 + Cadena2 + multilinea)
#Cadenas y repeticion 
eco="ja"*3
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre='Dulce'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#Remplazar texto en una cadena 
frase="Me gusta programacion"
print(frase.replace("Programacion","Matematicas"))
#Formato de concatenar cadenas de valores (F-String)
edad=16
Nombre='Dulce'
mensaje=f"Hola, me llamo {Nombre} y tengo\n{edad}años"
print(mensaje)
#Contar los caracteres de una cadena 
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto tiene una palabra 
oracion="Aprender python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
    print("No esta")
#Validar contenido de una cadena 
ncadena="12"
print(ncadena.isalpha())#True
print(ncadena.isalpha())#false
