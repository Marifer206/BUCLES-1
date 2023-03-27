numero = int(input("Ingrese un número entre 2 y 50: ")) # Pedir al usuario que le de valor a la variable numero entre 2 y 50
while numero < 2 or numero > 50: # Mientras que numero sea menor a 2 y mayor a 50
    print("Número inválido, intente de nuevo.")
    numero = int(input("Ingrese un número entre 2 y 50: "))

divisores = [] # Inicializar una lista vacía para los divisores
i = 1 # Inicializar un i en 1

while i <= numero: # mientras que i sea menor o igual a numero
    if numero % i == 0:
        divisores.append(i)
    i += 1 # actualizar variable para el siguiente numero

print(f"Los divisores de {numero} son: {divisores}") # imprimir los divisores de numero
