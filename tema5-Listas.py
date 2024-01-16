'''
Una lista es una secuencia de elementos.
1.- Se crea con corchetes []
2.- Es un inmutable 
3.- Puede usar diferentes tipos de datos

'''

#Crear una lista
lista1 = ["Roberto", 33, 9.5, True, "German", 20.8]

#Acceder a una lista por su posicion
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])


lista1.append("Vargas")
print(lista1)

lista1.insert(2, "Nadia")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(33)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2
print(lista3)

print(lista2*4)

lista4 = [2, 1, 5, 4, 3]
print(lista4)

#Ordenar una lista
lista4.sort()
print(lista4)

# Borrar una posicion de una lista
del lista4[0]
print(lista4)
