def crear_archivo():
    f = open('nombre.extension', "w")
    f.close()

def leer_archivo_open():
    f = open('CSVs/Muerte_nacimientos_por_region.csv', "r")
    #Saltamos la primera linea
    next(f)
    for linea in f:
        periodo, tipo, region, numero = linea.rstrip("\n").split(",")
        print("Año: " + periodo + ", Tipo: " + tipo + ", Region: " + region + ", Numero: " + numero)
    f.close()

def leer_archivo_with():
    with open('CSVs/Muertes_por_sexo_y_edad.csv') as f:
        #Saltamos la primera linea
        next(f)
        for linea in f:
            periodo, sexo, edad, numero = linea.rstrip("\n").split(",")
            print("Año: " + periodo + ", Sexo: " + sexo + ", Edad: " + edad + ", Numero: " + numero)