#Concatenacion de arreglos.
array1=[1,2,3,4,5,6,7,8,9,10]
array2=[True,False,True,False,True,False,True,False,True,False]
array3 = array1+array2
print (array3)
#OJO para encontrar un dato en el arreglo!!
print ("Arturo" in array1)
print ("Arturo" in array2)
print ("Arturo" in array3) #Si no esta aparecera como un false
print (True in array2) #Aqui aparecera como true ya que si lo encontro
#AHora si deseamos saber la possicion del dato dentro de la lista.
print (array1.index(1))
array1.index(1)
#Ahora la cantidad de veces que se repite.
print (array1.count(1))
array1.count(1)
#PAra quitar los valores.
array1.remove(True)
print (array1)
array1.reverse()
print (array1)


