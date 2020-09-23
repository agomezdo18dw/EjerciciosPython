import random

def duplicado(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True

def aleatorio():
    lista = list()
    for n in range(0, 23):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

lista = aleatorio()
TieneDup = duplicado(lista)
print("La lista " + str(lista) + " tiene duplicados?")
if TieneDup == True:
    print("Si")
else:
    print("No")