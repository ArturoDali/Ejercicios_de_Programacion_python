#Porgrama de introduccion a listas 2 .

#Programa 2, podemos combinar datos en el array


array = ["Boxeo","Basquetball",123, 5.6, -9,True, False]
print (array [0])
print (array [1])
print (array [2])
print (array [3])
print (array [4])
print (array [5])
print (array [6])

#Ahora podemos tener una lista dentro de otra lista??
array = ["Boxeo","Basquetball",123, 5.6, -9,True, False,["Carlos","Carmen","Arturo","Luisa","Sanson","Carmelita"]]
print (array [0])
print (array [1])
print (array [2])
print (array [3])
print (array [4])
print (array [5])
print (array [6])
print (array [7]) #En este csao imprime toda la lista de nombres.

#Ahora para imprimir porbloques es decir por los indices, por ejemplo de 0 hasta el 2
print (array[0:2]) #Recuerda que omite el ultimo numero es decor el dos
print (array[:2])
print (array[0:])