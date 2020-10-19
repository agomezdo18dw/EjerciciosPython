__all__ = ['comprobar_nombre', 'mostrar_telefono']


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
    return agenda


amigos = ['Mikel', 'Leire', 'Patxi']
