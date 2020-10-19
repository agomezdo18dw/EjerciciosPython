def duplicado(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True

listas = [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0]]

for lista in listas:
    TieneDup = duplicado(lista)
    print("La lista " + str(lista) + " tiene duplicados?")
    if TieneDup == True:
        print("Si")
    else:
        print("No")