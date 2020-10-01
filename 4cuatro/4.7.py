def generar_n_caracteres(n, caracter):
    print(caracter * n)

print("--------------------------------------------------------------------")
print("Introduce un caracter y el numero de veces que quieres que se repita")
print("--------------------------------------------------------------------")

caracter = str(input("Introduce un caracter: "))
n = int(input("Introduce la cantidad de veces que se repetira: "))

generar_n_caracteres(n, caracter)
