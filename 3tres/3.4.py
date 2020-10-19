import os

def suma(a, b):
    print("-------------------------")
    print("La suma es: " + str( a + b ))
    print("-------------------------")
    print("")

def resta(a, b):
    print("-------------------------")
    print("La resta es: " + str( a - b ))
    print("-------------------------")
    print("")

def multiplicacion(a, b):
    print("-------------------------")
    print("La multiplicacion es: " + str( a * b ))
    print("-------------------------")
    print("")

def division(a, b):
    if b > a:
        resultado = b / a
    else:
        resultado = a / b

    print("-------------------------")
    print("La division es: " + str( resultado ))
    print("-------------------------")
    print("")

def resto(a, b):
    if b > a:
        resultado = b % a
    else:
        resultado = a % b

    print("-------------------------")
    print("El resto es: " + str( resultado ))
    print("-------------------------")
    print("")

while True:
    # os.system('clear')
    print("CALCULADORA")
    print("-------------------------")
    print("Escribe un numero:")
    a = int(input())
    print("Escribe otro numero:")
    b = int(input())
    print("")
    print("Pulsa el numero de la operacion que quieras realizar:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Resto")
    print("6 - Elegir otros numeros")
    print("7 - Cerrar")
    operacion = int(input("Numero: "))

    if operacion == 1:
        suma(a, b)
    elif operacion == 2:
        resta(a, b)
    elif operacion == 3:
        multiplicacion(a, b)
    elif operacion == 4:
        division(a, b)
    elif operacion == 5:
        resto(a, b)
    elif operacion == 6:
        os.system('clear')
        continue
    elif operacion == 7:
        print("Cerrando...")
        exit()
