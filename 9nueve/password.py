class Password(object):

    def __init__(self, longitud=8):
        self.longitud = longitud
        self.contraseña = self.generarPassword()

    def generarPassword(self):
        import random
        password = ''
        caracteresLower = 'adbcdefghijklmnñopqrstuvwxyz'
        caracteresUpper = caracteresLower.upper()
        caracteresNums = '0123456789'
        caracteres = caracteresLower + caracteresUpper + caracteresNums

        for _ in range(self.longitud):
            letra = random.choice(caracteres)
            password += letra

        return password

    def esFuerte(self):
        fuerte = False
        mayus = 0
        minus = 0
        nums = 0
        for caracter in self.contraseña:
            if caracter.isupper():
                mayus += 1
                continue
            if caracter.islower():
                minus += 1
                continue
            if caracter.isdigit():
                nums += 1
                continue

        if mayus > 2 and minus > 1 and nums > 5:
            fuerte = True

        return fuerte


class HeredaPassword(Password):

    def __init__(self):
        self.listapassword = []
    
    def cargarListaPassword(self, cantidadContraseñas):
        import random
        for _ in range(cantidadContraseñas):
            longitud = random.randint(20,30)
            self.listapassword.append(Password(longitud))

    def crearListaFuerte(self):
        listafuerte = []
        for contraseña in self.listapassword:
            esFuerte = contraseña.esFuerte()
            listafuerte.append(esFuerte)
        return listafuerte
         

    def imprimirListaFuerte(self, listaFuerte):
        for contraseña, esFuerte in zip(self.listapassword, listaFuerte):
            print("Password: {a: >30}, ¿Es fuerte?: {b: >2}".format(a=contraseña.contraseña, b=str(esFuerte)))


p=HeredaPassword()
p.cargarListaPassword(10)
p.imprimirListaFuerte(p.crearListaFuerte())