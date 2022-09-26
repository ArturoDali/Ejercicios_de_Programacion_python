#En este ejercicio se debend e ingresar ter numeros y determinar cual es el mayor.
#En este ejercicio se deben de comaprar tres nuemros desde la consola.

n1=int(input("Ingresa le primer nuemro: "))
n2=int(input("Ingresa le primer nuemro: "))
n3=int(input("Ingresa le primer nuemro: "))

if n1>=n2 and n1 >=n3:
    print ("El numero mayor es el uno")
elif n2>=n1 and n2 >=n3:
    print ("El numero mayor es el dos")
elif n3>=n1 and n3 >=n2:
    print ("El numero mayor es el tres")
else:
    print ("No metiste un nuemero")
