#Ejercicio de practica obteniendo algunos porcentajes.
# Porblea Francisco compro unos tenis de 1200 pesos, pero le hicieron un desciento del 25%, programelos, 
#que el programa solo te pida el precio del producto y te de el 25 % de descuento por default.

print ("Welcome")

a=float (input("Indica el precio de la compra"))
descuento= a*(25/100)
preciofinal = a - descuento
print (f"El precio fona es : {preciofinal}")
