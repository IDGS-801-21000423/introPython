print("Suma de numeros")

num1 = int(input("Dame un valor1: "))
num2 = int(input("Dame un valor2: "))

if num1 > num2:
  print("el {} es mayor que el {}".format(num1, num2))
else :
  print("el {} es mayor que el {}".format(num2, num1))
  

print("--------------------- Pedir una edad --------------------- ")

edad = int(input("Ingresa tu edad: "))

if edad > 18:
  print("Eres mayor de edad")
elif edad == 18:
  print("Eres mayor de edad")
else:
  print("No eres mayor de edad")

