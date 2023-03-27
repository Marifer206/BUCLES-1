import math # Importar el módulo math

def es_primo(numero):
    if numero < 2: # Si el número es menor que 2, no es primo
        return False
    i = 2 # Inicializa i en 2 ( i es el divisor )
    while i <= int(math.sqrt(numero)): # Mientras el divisor sea menor o igual que la raíz cuadrada del número
        if numero % i == 0: # Si el número es divisible por el divisor actual
            return False # El número no es primo
        i += 1 # Incremnetar de 1 en 1 el divisor
    return True # Si ningún divisor lo divide, el número es primo

if __name__ == "__main__":
    numero = 1  # Inicializa a numero ( primer número a comprobar ) 
    while numero <= 100:  # mientras el número sea menor o igual a 100
        if es_primo(numero): # si el número es primo ( se llama a la funcion )
            print(numero, end=", ") # Imprime el número en la misma línea, separado por una coma
        numero += 1 # incrementa el número a comprobar en 1 para pasar al siguiente
