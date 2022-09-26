#Coincidencia en un par de nombres
#Crear un programa que comapre dos nombres , y verificar su hay coincidencias o no
#si es que ambos nombres comienzan con la misma letra, o terminana con la misma letra.
nombre1=input("Ingresa el nombre numero 1: ")
nombre2=input("Ingresa el nombre numero 2: ")

if nombre1==nombre2:
    print ("Si hay coincidencia son iguales")
elif nombre1[0] == nombre2[0]:
    print ("Inician con la misma letra ambos nombres")
elif nombre2[-1] ==nombre2[-1]:
    print ("Terminan con la misma letra")
else :
    print ("No hay coincidencias")