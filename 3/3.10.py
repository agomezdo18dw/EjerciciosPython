def multiplicacion(lista):
    result = 1
    for n in lista:
        result *= n
    return result

print("--------------------------------------------")
print("Introduce numeros hasta que introduzcas un 0")
print("--------------------------------------------")

numeros = []
while True:
    num = int(input("Introduce un numero: "))
    if num != 0:
        numeros.append(num)
    elif :

    else:
        print()
        print('------------------')
        print('Informacion:')
        print('Numero mas alto: ' + str(max(numeros)))
        print('Numero mas bajo: ' + str(min(numeros)))
        print('Cantidad de numeros introducida: ' + str(len(numeros)))
        print('Suma de todos los numeros: ' + str(sum(numeros)))
        print('Multiplicacion de todos los numeros: ' + str(multiplicacion(numeros)))
