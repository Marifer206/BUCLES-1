import math # importar modulo math
x : int = 0 # inicializa la variable x en 0
while (x <= 100) : # mientras x sea menor o igual a 100
    x +=1 # incrementa el valor de x en 1
    if x == 101:# si x es igual a 101, se salta al siguiente ciclo
        continue
    n:int = math.pow (x,2) # calcula el cuadrado de x y lo almacena en la variable n
    print("el cuadrado de " + str(x) + " es " + str(n) ) # imprime el resultado del cuadrado de x