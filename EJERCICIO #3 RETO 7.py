num : int = 0 # inicializa num en 0
while num < 65 or num > 90: # mientras sea menor de 65 o mayor de 90
  num = int(input("Ingrese un entero: ")) # usuario mete el numero entero
  print("El entero " + str(num) + " corresponde al caracter " + chr(num)) # Caracter que corresponde al numero