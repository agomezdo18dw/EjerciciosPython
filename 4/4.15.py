def contar_vocales(palabra):
    Va = 0
    Ve = 0
    Vi = 0
    Vo = 0
    Vu = 0
    for letra in palabra:
        if letra in "aA":
            Va += 1
        elif letra in "eE":
            Ve += 1
        elif letra in "iI":
            Vi += 1
        elif letra in "oO":
            Vo += 1
        elif letra in "uU":
            Vu += 1
    print("La palabra " + palabra + " tiene:")
    print("Letra(s) a: " + str(Va))
    print("Letra(s) e: " + str(Ve))
    print("Letra(s) i: " + str(Vi))
    print("Letra(s) o: " + str(Vo))
    print("Letra(s) e: " + str(Vu))

print("------------------------------------------------------------")
print("Introduce una palabra para ver cuantas vocales de cada tiene")
print("------------------------------------------------------------")

palabra = str(input("Introduce una palabra: "))

contar_vocales(palabra)
