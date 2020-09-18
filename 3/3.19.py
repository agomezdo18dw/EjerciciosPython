for num in range(2, 10):
    # Ejecuta el codigo 8 veces cogiendo numeros entre el 2 y el 10
    if num % 2 == 0:
        # Si el resto del numero por el que va el bucle / 2 es 0 muestra el print de abajo y luego ejecuta la siguiente iteracion del for
        print('Encontre un numero par', num)
        continue
        # Si no encuentra un numero / 2 que el resto sea 0 muestra el print de abajo
    print('Encontré un numero', num)
