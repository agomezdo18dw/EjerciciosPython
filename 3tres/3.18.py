for n in range(2, 10):
    # Ejecuta el codigo 8 veces cogiendo numeros entre el 2 y el 10
    for x in range(2, n):
        # Por cada vez que se ejecuta trata de ejecutar un maximo de veces igual al numero por el que va el for anterior empezando por el 2
        if n % x == 0:
            # Si el resto de n/x es 0 dice el print de abajo y luego da por concluido el for volviendo a la siguiente iteracion del primero
            print(n, 'es igual a', x, '*', n/x)
            break
    else:
        # Si nada de dentro del for se cumple ejecuta el else diciendo lo que dice el print de abajo
        print(n, 'es un numero primo')
