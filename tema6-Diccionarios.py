#Creacion de un diccionario
miDiccionario = {
  "Matricula": 12345, 
  "Nombre": "Jose",
  "Appelidos": "Ramos"
}

#Acceder a una propiedad de un diccionario
print(miDiccionario["Nombre"])

print(miDiccionario)

#Saber el tipo de una variable
print(type(miDiccionario))

#Cambiar el valor de una propiedad
miDiccionario["Nombre"]="Dario"
print(miDiccionario)

#Agregar el valor a un elemento y agregarlo al diccionario
miDiccionario["correo"]="dario.gmail.com"
print(miDiccionario)

