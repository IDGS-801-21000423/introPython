num1 = 20
num2 = 4

print("La suma es: ", (num1+num2))
print("La resta es: ", (num1-num2))
print("La multiplicacion es: ", (num1*num2))
print("La divison es: ", (num1/num2))
print("La divison exacta es: ", (num1//num2))
print("La potencia es: ", (num1 ** num2))

#Concatenacion en python

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " "+ texto2  + "Mundo"
print(textoFinal)


print("El saludo es: % % " %{texto1, texto2})

saludoFinal = "Saludo {} {}".format(texto1, texto2)
print(saludoFinal)

saludoFinal = "Saludo 2: {y} {x}".format(y=texto1, x=texto2)
print(saludoFinal)