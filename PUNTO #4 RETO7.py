# inicializamos variables
a = 25 # Población inicial del país A en millones
b = 18.9 # Población inicial del país B en millones
crecimiento_a = 0.02 # Tasa de crecimiento anual del país A
crecimiento_b = 0.03 # Tasa de crecimiento anual del país B
year = 2022 # Año inicial

while b <= a: # Mientras la población del país B sea menor o igual que la del pais A
    a += a * crecimiento_a # Se suma la cantidad de personas segun la tasa de crecimiento anual
    b += b * crecimiento_b # Se suma la cantidad de personas segun la tasa de crecimiento anual
    year += 1 # Aumenta de 1 en 1 para evaluar el crecimiento anual
    
print(f"La población del país B superará a la del país A en el año {year} con una poblacion " + str( b ) +" millones frente a una poblacion de " + str( a ) + " millones de el pais A") # Imprime el año en que la población de B supera a la de A
