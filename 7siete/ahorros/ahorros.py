import csv

# 7.4
def guardar_ahorros():
    """ Guarda la lista de puntajes en el archivo.
    Pre: nombre_archivo corresponde a un archivo válido,
    puntajes corresponde a una lista de secuencias de elementos.
    Post: se guardaron los valores en el archivo,
    separados por comas.
    """
    archivo = open('ahorros.txt', "w", newline='')
    archivo_csv = csv.writer(archivo)
    ahorros = [
       #('nombre',          'edad', 'cantidad (€)'),
        ('Aitor Iturbe',       '8',       '115.05'),
        ('Leire Amarra',       '5',         '0.93'),
        ('Inaxio Aguirre',    '10',         '21.2'),
        ('Maddi Iturbe',       '8',        '90.23'),
        ('Enaut Beobide',      '7',       '123.83')
    ]
    archivo_csv.writerows(ahorros)
    archivo.close()

# 7.5
def ver_ahorros():
    ahorros = []
    archivo = open('ahorros.txt', 'r')
    archivo_csv = csv.reader(archivo)
    for nombre, edad, cantidad in archivo_csv:
        ahorros.append((nombre, edad, cantidad))
    archivo.close()
    print(ahorros)


# 7.6
def ver_ahorros_with():
    with open('ahorros.txt') as f:
        print(f.read())


# 7.7
def ver_ahorros_list():
    f = open('ahorros.txt', 'r')
    lista = list()
    for fila in f:
        lista.append(fila.rstrip('\n'))
    f.close()
    #print(lista)
    return lista

def ver_ahorros_readlines():
    f = open('ahorros.txt', 'r')
    print(f.readlines())
    f.close()


# 7.8
def visualizar():
    f = open('ahorros.txt', 'r')
    for linea in f:
        nombre, edad, cantidad = linea.rstrip("\n").split(",")
        print(nombre + ", de " + edad + " años de edad, ha ahorrado la cantidad de " + cantidad + "€" )
    f.close()


# 7.9


# 7.10
def leer_binario():
    f = open('ahorros.txt', 'rb')
    i = 0
    while i < 4:
        byte_ = f.read(i)
        print(byte_)
        i += 1
    print("Posicion del puntero: "+str(f.tell()))
    print("Muevo el puntero a la posicion 30")
    f.seek(30)
    i = 0
    while i < 4:
        byte_ = f.read(i)
        print(byte_)
        i += 1
    print("Posicion del puntero: "+str(f.tell()))
    f.close()


# 7.12
def lista_json():
    import json
    lista = ver_ahorros_list()
    json = json.dumps(lista)
    #print(json)
    return json


# 7.13
def serializar():
    import json
    lista = ver_ahorros_list()
    f = open('ahorros.json', "w")
    json.dump(lista, f)
    f.close()


# 7.15
def deserializar():
    import json
    f = open('ahorros.json', "r")
    json = json.load(f)
    l = list(json)
    f.close()
    #print(l)
    return l


# 7.16
def lista_json2():
    import json
    deserializado = deserializar()
    json = json.dumps(deserializado)
    print(json)
    print(lista_json())


# 7.18
def head(archivo, n):
    i = 1
    with open(archivo) as lineas:
        for linea in lineas:
            print(linea.rstrip("\n"))
            if i == n:
                break
            i += 1
            

# 7.19
def cp(archivo):
    f = open(archivo, "r")
    nombre_cp = archivo.split(".")
    nuevo_nombre = str(nombre_cp[0])+"_cp."+str(nombre_cp[1])
    cp_archivo = open(nuevo_nombre, "w")
    for linea in f:
        cp_archivo.write(linea)
    f.close()
    cp_archivo.close()
            

