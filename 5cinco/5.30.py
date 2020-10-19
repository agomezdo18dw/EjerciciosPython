def comprobar_nombre(agenda, nombre):
    if nombre in agenda:
        return True
    else:
        return False


def mostrar_telefono(agenda, nombre):
    print("El numero de " + nombre + " es: " + agenda[nombre])
    modificar = str(input("¿Desea modificar el telefono?(S/N)"))
    modificar = modificar.lower()
    if modificar == 's':
        guardar_telefono(agenda, nombre)


def guardar_telefono(agenda, nombre):
    tel = str(input("Escribe el telefono de " + nombre + ": "))
    agenda[nombre] = tel
    print("Guardando telefono de " + nombre + "...")
    #return agenda


print("------")
print("AGENDA")
print("------")

agenda = {}

while True:
    print()
    nombre = str(input("Escribe un nombre('*' para salir): "))
    if nombre == "*":
        exit()
    else:
        nombre = nombre.capitalize()
        existe_nombre = comprobar_nombre(agenda, nombre)
        if existe_nombre:
            mostrar_telefono(agenda, nombre)
        else:
            guardar_telefono(agenda, nombre)
