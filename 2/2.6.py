def area(l1, l2, l3):
    sp = (l1 + l2 + l3)/2
    area = sp ** (1.0/2) * ((sp - l1) * (sp - l2) * (sp - l3))
    return area

print("--------------------------------------------")
print("Introduce tres lados del triangulo para calcular su area")
print("--------------------------------------------")

while True:
    l1 = float(input("Introduce el primer lado: "))
    l2 = float(input("Introduce el segundo lado: "))
    l3 = float(input("Introduce el tercer lado: "))

    print('El area del triagulo es ' + str(area(l1, l2, l3)))
    print('')
