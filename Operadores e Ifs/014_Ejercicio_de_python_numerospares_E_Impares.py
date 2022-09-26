#Ejercicio de numeros pares e impares.
n1=int(input("Ingresa el primer nuemro: "))
n2=int(input("Ingresa el segundo numero: "))

if n1%2==0 and n2%2==0:
    print (" Ambos numeros son pares ")
elif n1%2==0 and n2%2!=0:
    print ("El primero numero es par")
    print ("El segundo numero es impar")
elif n1%2!=0 and n2%2==0:
    print ("El primer nuemro es impar.")
    print ("El segundo numero es par")
else :
    print ("Recuerda que el cero no es divisible")