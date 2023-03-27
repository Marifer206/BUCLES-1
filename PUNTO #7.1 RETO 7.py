divisores = [] # Creamos una lista vacia para los divisores
x = int(input("Ingrese el número del cual quiera saber sus divisores: ")) # Inicializamos variable con valor (numero entero) dado por el usuario 
i = 1 # inicializamos i en 1
while i <= x: # mientras i sea menor o igual a x
    if x % i == 0: 
        divisores.append(i)
    i += 1 # Actualizamos variable para continuar evaluando el siguiente numero 
print("Los divisores de " + str(x) + " son " + str(divisores)) # imprimimos resulado de los divisoes de x