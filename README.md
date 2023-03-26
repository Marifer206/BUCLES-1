# BUCLES-1 :star:
REALIZANDO NUESTRO RETO #7

## 1.EJERCICIOS DE CLASE
### EJERCICIO #1  :space_invader:
Diseñe un algoritmo que involucre un ciclo y que nunca ingrese al ciclo.

#### CODIGO DEL PROGRAMA

```ruby
x:int = 25 #<inicia>
print('El valor inicial de x es '+ str(x))
while(x <= 24): #<cond>
  print('El valor de x durante el ciclo') #<bloque>
  x = x + 1 #<actualiza> 
print('El valor final de x es '+ str(x))
```

:checkered_flag: El programa ejecutado se ve asi

<div align='center'>
<figure> <img src="https://i.postimg.cc/50tbzBmq/image.png" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i>x</i> no ingresa al ciclo</b></figcaption></figure>
</div>


### EJERCICIO #2  :space_invader:
Diseñe un algoritmo que involucre un ciclo y que se ejecute indefinidamente.

#### CODIGO DEL PROGRAMA
```ruby
a = 1 # inicializa a en 1
b = 10 # inicializa b en 10
print('El valor inicial de a es '+ str(a) +'y de b es '+ str(a)) # valores iniciales de a y b 
while a < b: # mientras a sea menor a b
  print(a, b, sep = ", ") # imprime los valores de a y b usando el parametro separador 
  a += 1 # a = a + 1; i se incrementa de 1 en 1
  b += 10 # b = b + 10; se incrementa de 10 en 10
print("EL FIIIN.") # se ejecuta al terminar el ciclo
print(a, b, sep = ", ") # valores finales de a y b
```

:checkered_flag: El programa ejecutado se ve asi

<div align='center'>
<figure> <img src="https://i.postimg.cc/wjZm0kv2/image.png" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i>a y b</i> ingresan al ciclo y se ejecutan indefinamente</b></figcaption></figure>
</div>

### EJERCICIO #3  :space_invader:
Diseñe un algoritmo que pida un valor entero, y que siga leyendo valores enteros mientras que alguno de esos valores no represente el código ASCII de una letra mayúscula en el abc del inglés.

<div align='center'>
<figure> <img src="https://i.postimg.cc/7hH1sGJ1/image.png" alt="" width="600" height="auto"/></br>
<figcaption><b>Tabla de caracteres con equivalente en ASCII.</b></figcaption></figure>
</div>

#### CODIGO DEL PROGRAMA
```ruby
num : int = 0 # inicializa num en 0
while num < 65 or num > 90: # mientras sea menor de 65 o mayor de 90
  num = int(input("Ingrese un entero: ")) # usuario mete el numero entero
  print("El entero " + str(num) + " corresponde al caracter " + chr(num)) # Caracter que corresponde al numero
```

:checkered_flag: El programa ejecutado se ve asi

<div align='center'>
<figure> <img src="https://i.postimg.cc/v83k77GM/image.png" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> num </i> ingresan al ciclo y se ejecuta hasta que corresponda a una letra en mayuscula en el código ASCII </b></figcaption></figure>
</div>


## PUNTOS DEL RETO
### PUNTO #1  :space_invader:
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#### CODIGO DEL PROGRAMA
```ruby
import math
x : int = 0 # inicializa la variable x en 0
while (x <= 100) : # mientras x sea menor o igual a 100
    x +=1 # incrementa el valor de x en 1
    if x == 101:# si x es igual a 101, se salta al siguiente ciclo
        continue
    n:int = math.pow (x,2) # calcula el cuadrado de x y lo almacena en la variable n
    print("el cuadrado de " + str(x) + " es " + str(n) ) # imprime el resultado del cuadrado de x

```
:checkered_flag: El programa ejecutado se ve asi

<div align='center'>
<figure> <img src="https://i.postimg.cc/1tXk1zQn/image.png" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> X </i> ingresan al ciclo y se ejecuta hasta hacer un listado de 1 al 100 con sus respectivos cuadrados</b></figcaption></figure>
</div>

### PUNTO #2  :space_invader:
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


#### CODIGO DEL PROGRAMA
```ruby
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
```
:checkered_flag: El programa ejecutado se ve asi

<div align='center'>
<figure> <img src="https://i.postimg.cc/pdnmPKtz/image.png" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> X </i> ingresan al ciclo y se ejecuta hasta hacer un listado de numeros pares hasta 1000 y otro de numeros impares hasta 999</b></figcaption></figure>
</div>

### PUNTO #3  :space_invader:
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado


#### CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: El programa ejecutado se ve asi



### PUNTO #4  :space_invader:
En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.


#### CODIGO DEL PROGRAMA
```ruby

```
:checkered_flag: El programa ejecutado se ve asi



### PUNTO #5  :space_invader:
Imprimir el factorial de un número natural n dado.


#### CODIGO DEL PROGRAMA
```ruby

```
:checkered_flag: El programa ejecutado se ve asi


### PUNTO #6  :space_invader:
Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.


#### CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: El programa ejecutado se ve asi




### PUNTO #7  :space_invader:
Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

```ruby

```

:checkered_flag: El programa ejecutado se ve asi


### PUNTO #8  :space_invader:
Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

```ruby

```
