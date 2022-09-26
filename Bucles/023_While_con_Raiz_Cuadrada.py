#Programa con raiz cuadrada
import math
numero =int(input("Ingresa un numero para obtener la ráiz: "))
while numero <0:
    print ("Ingrese un numero positivo.")
    numero = int(input("Vuelva a ingresar un numero: "))
print (f"El numero de la raíz cuadrada es :{math.sqrt(numero)}")