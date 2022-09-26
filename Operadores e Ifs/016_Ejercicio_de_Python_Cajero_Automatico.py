#Ejercicio de cajero automatico.
#Crear un programa que simule un cajero automatico, con un saldo inicial de 2000 cob ek siguiente menu:
#Ingreso de dinero
#Retirar dienero
#Mostrar Dinero
#Salir


saldo=2000
print ("**** WELCOME ****")
print ("1.- Ingresa dinero: ")
print ("2.- Retirar dienro: ")
print ("3.- Mostrar dinero: ")
print ("4.- Salir")

seleccion = int (input( "Ingresa una opcion: "))
if seleccion ==1 :
    ingreso1=int(input("Cantidad a ingresar."))
    saldofinal= saldo+ingreso1
    print (f"El saldo disponible es {saldofinal}")
elif seleccion ==2 :
    salida1=int(input("Ingrese la cantidad a retirar: "))
    if salida1>saldo:
        print ("No puedes retirar esa cantidad, tienes menos en tu cuenta")
    else:
        saldofinal=saldo-salida1
        print ("Retiro ",salida1)
elif seleccion ==3:
    print ("Usted tiene",saldo)
elif seleccion ==4 :
    print ("FIn")
else :
    print ("Error ")
