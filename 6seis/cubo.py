"""Programa de calculo del cubo de un numero"""

__author__ = "Adrigo"
__copyright__ = "adrigo.es"
__credits__ = ["Ander"]
__version__ = "1.0"

def cubo(x):
    """Calcula el cubo de un numero"""
    y = x ** 3
    return y


if __name__ == "__main__":
    """Calcula el cubo de un numero"""
    x = int(input("Dame un numero: "))
    y = cubo(x)
    print ("El cubo de %.2f es %.2f" % (x, y))
