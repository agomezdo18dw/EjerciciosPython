def elimina_duplicados(lista):
    return list(set(lista))

lista = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
print(elimina_duplicados(lista))