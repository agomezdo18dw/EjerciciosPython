import json


def guardar_datos(peticiones_solicitud, atenciones):
    try:
        nombre = str(input("Introduce el nombre del archivo donde desea guardar los datos sin extension (se crea un JSON): "))
        estructura = {
            'peticiones': peticiones_solicitud,
            'atenciones': atenciones
        }
        f = open(nombre+'.json', "w")
        json.dump(estructura, f)
        f.close()
        print("Datos guardados en el archivo "+nombre+".json")
    except OSError:
        print("Hubo un error a la hora de guardar los datos.")
    finally:
        print()

def leer_datos():
    try:
        nombre = str(input("Introduce el nombre del archivo del que desea leer los datos sin extension: "))
        f = open(nombre+'.json', "r")
        datos = json.load(f)
        f.close()
        print("Datos importados correctamente")
    except OSError:
        print("""
 -----------------------
| ¡El archivo no existe! |
 -----------------------
        """)
        datos = {
            'peticiones': 0,
            'atenciones': 0,
        }
    finally:
        print()
        return datos

