while True: # Utilizamos la sentencia while true para hacer un bucle infinito hasta encontrar un break
    inicio = input("Piensa un numero entre el rango del 1 al 100 escibe 'ya' si estas listo ")
    if inicio == "ya":
        print("te hare una serie de preguntas responde 's' para si y n para 'no'") # Detalles para que parezca un juego
    else:
        print("Respuesta inválida, intente de nuevo.")
        continue

    # Definir las constantes para el rango de búsqueda
    RANGO_MINIMO = 1
    RANGO_MAXIMO = 100

    # Inicializar las variables para la búsqueda
    minimo = RANGO_MINIMO
    maximo = RANGO_MAXIMO
    intentos = 0

    while minimo <= maximo: # mientras el minimo sea menor o igual que el maximo
        intentos += 1  # Incrementar el contador de intento
    
        medio = (minimo + maximo) // 2 # Adivinar el número medio del rango actual
        respuesta = input(f"¿Es {medio} el número? (s/n) ")

        # Actualizar el rango de búsqueda según la respuesta
        if respuesta == "s": 
            print(f"¡Adiviné el número en {intentos} intentos!")
            break
        elif respuesta == "n":
            respuesta = input(f"¿Es el número mayor o menor que {medio}? (mayor/menor) ")
            if respuesta == "mayor":
                minimo = medio + 1
            elif respuesta == "menor":
                maximo = medio - 1
            else:
                print("Respuesta inválida, intente de nuevo.")
        else:
            print("Respuesta inválida, intente de nuevo.")

    # Preguntar al usuario si desea jugar nuevamente
    jugar_nuevamente = input("¿Desea jugar nuevamente? (s/n) ")
    if jugar_nuevamente != "s":
        break