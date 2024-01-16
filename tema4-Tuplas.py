'''
Las tuplas son Inmutables
'''

#Creacion de una Tupla
tupla = ("uno", "dos", "tres")

print(tupla)

#Creacion de una Tupla con Varios Datos
tuplasVariosDatos = (12, True, 23.5, "El gato", 12+3)
print(tuplasVariosDatos)


#Creacion de una Tupla con una Tupla dentro
tuplasConTuplas = (1, 2, 3, 4, (1, 2 ,3))
print(tuplasConTuplas)

#Acceder a la posicion de una tupla
print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])
print(tuplasVariosDatos[0:2])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaNueva = tupla + tuplasVariosDatos
print(tuplaNueva)

