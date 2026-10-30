try:
   numero1=int(input("Ingresan el primer numero"))
   numero1=int(input("Ingresan el segundo numero"))
   resultado=numero 1/ numero 2
except ZeroDivisionError:
    print("Solo introduce numeros")
except ValueError:
    print("Division entre cero")
else:
    print("El resultado es ",resultado)
finally:
    print("Programa finalizado")
