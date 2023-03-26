pares = [] # Crea una lista vacía para los números pares
n = int(input("Ingrese un número natural mayor o igual a 2: ")) # Declara e inicializa variable con valor dado por el usuario
# Imprime los números pares en forma descendente hasta 2
while n >= 2: # Mientras que n sea mayor o igual a 2
    pares.append(n)
    n -= 2 # Disminuye de dos en dos para que pueda imprimirse de manera descendente
    if n % 2 != 0: # Descarta los numeros impares
        continue
print("Numeros pares de forma descendente " + str(pares)) # Imprime la lista pares en forma descendente hasta 2
