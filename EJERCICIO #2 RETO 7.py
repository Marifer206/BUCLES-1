a = 1 # inicializa a en 1
b = 10 # inicializa b en 10
print('El valor inicial de a es '+ str(a) +'y de b es '+ str(a)) # valores iniciales de a y b 
while a < b: # mientras a sea menor a b
  print(a, b, sep = ", ") # imprime los valores de a y b usando el parametro separador 
  a += 1 # a = a + 1; i se incrementa de 1 en 1
  b += 10 # b = b + 10; se incrementa de 10 en 10
print("EL FIIIN.") # se ejecuta al terminar el ciclo
print(a, b, sep = ", ") # valores finales de a y b