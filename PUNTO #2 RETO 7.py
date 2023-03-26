pares = [] # crea una lista vacía para los números pares
impares = [] # crea una lista vacía para los números impares
x : int = 0 # inicializa la variable x en 0
while (x <= 1000) : # mientras x sea menor o igual a 1000
    x +=1 # incrementa el valor de x en 1
    if x == 1001:# si x es igual a 1001, se salta al siguiente ciclo
        continue
    if x % 2 == 0 :# si el residuo de la division es igual a 0 es par
         pares.append(x)
    else:
        x % 2 != 0 # si el residuo de la division no es igual a 0 es impar
        impares.append(x)
print("Numeros Pares " + str(pares)) # imprime la lista de pares
print("Numeros Impares" + str(impares)) # imprime la lista de impares