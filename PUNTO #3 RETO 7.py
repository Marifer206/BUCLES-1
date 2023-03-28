pares = [] # Crea una lista vacía para los números pares
n = int(input("Ingrese un número natural mayor o igual a 2: ")) # Declara e inicializa variable con valor dado por el usuario
# Imprime los números pares en forma descendente hasta 2
while n >= 2: # Mientras que n sea mayor o igual a 2
    if n % 2 == 0:
        pares.append(n)
        n -= 2
    if n % 2 != 0:
        n-=1
print("Numeros pares de forma descendente " + str(pares)) # Imprime la lista pares en forma descendente hasta 2
