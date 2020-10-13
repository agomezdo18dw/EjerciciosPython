import sys


class Caracteres(Exception):
    """Excepcion para mas de un caracter."""
    pass


class NoCaracter(Exception):
    """Excepcion para ningun caracter."""
    pass


def generar_n_caracteres(n, caracter):
    '''Escribe un caracter dado tantas veces como se le diga.'''
    if len(caracter) == 1:
        print(caracter * n)
    elif len(caracter) == 0:
        raise NoCaracter("Ningun caracter")
    else:
        raise Caracteres


print("--------------------------------------------------------------------")
print("Introduce un caracter y el numero de veces que quieres que se repita")
print("--------------------------------------------------------------------")

try:
    caracter = str(input("Introduce un caracter: "))
    n = int(input("Introduce la cantidad de veces que se repetira: "))

    generar_n_caracteres(n, caracter)
except ValueError:
    print("!Ha ingresado un valor incorrecto¡")
except Caracteres:
    print("Probando excepciones propias")
except:
    e = sys.exc_info()[0]
    print("Tipo de excepcion: " + str(e))
else:
    print("El programa no dio excepciones.")
finally:
    print("Cerrando programa...")
