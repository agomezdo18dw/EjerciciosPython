def contar_vocales(palabra):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in palabra:
        if letra in "aA":
            vocales['a'] += 1
        elif letra in "eE":
            vocales['e'] += 1
        elif letra in "iI":
            vocales['i'] += 1
        elif letra in "oO":
            vocales['o'] += 1
        elif letra in "uU":
            vocales['u'] += 1
    print('')
    print("La palabra '" + palabra + "' tiene:")
    print("Letra(s) a: " + str(vocales['a']))
    print("Letra(s) e: " + str(vocales['e']))
    print("Letra(s) i: " + str(vocales['i']))
    print("Letra(s) o: " + str(vocales['o']))
    print("Letra(s) e: " + str(vocales['u']))

print("------------------------------------------------------------")
print("Introduce una palabra para ver cuantas vocales de cada tiene")
print("------------------------------------------------------------")

palabra = str(input("Introduce una palabra: "))

contar_vocales(palabra)
