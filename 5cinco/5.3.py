def sum(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sum(lista[1:])

def multip(lista):
    result = 1
    for num in lista:
        result *= num
    return result

lista = [1,2,3,4]
print("La suma y la multiplicacion de la lista: " + str(lista))
print("Suma: " + str(sum(lista)))
print("multiplicacion: " + str(multip(lista)))
print()
