from datetime import date
import leer_guardar as lg

peticiones_solicitud = {}
atenciones = {}


def registrar_numero_peticion_atencion(peticiones_solicitud):
    num_correlativo = len(peticiones_solicitud)
    codigo_postal = int(input("Introduce el codigo postal: "))
    fecha = str(date.today())
    peticiones_solicitud[num_correlativo] = {
        'cod_postal': codigo_postal,
        'fecha': fecha}
    print()


def registrar_atencion_cliente(peticiones_solicitud, atenciones):
    num_correlativo = int(input("Peticion atendida: "))
    num_correlativo = num_correlativo-1
    if num_correlativo not in peticiones_solicitud:
        print('Esa solicitud no existe')
        print()
        return None
    if num_correlativo in atenciones:
        print('Esa solicitud ya ha sido atendida')
        print()
        return None
    cod_empleado = str(
        input("Codigo del empleado(-1 si no se quiere especificar): "))
    if cod_empleado == '-1':
        cod_empleado == None
    tiempo_empleado = int(
        input("Tiempo empleado en minutos(0 si no se quiere especificar): "))
    if tiempo_empleado == 0:
        tiempo_empleado = None
    tipo = str(input("Tipo de operacion(Venta o informacion): "))
    fecha = str(date.today())
    codigo_postal = peticiones_solicitud[num_correlativo]['cod_postal']
    atenciones[num_correlativo] = {'cod_empleado': cod_empleado,
                                   'tiempo_empleado': tiempo_empleado,
                                   'tipo': tipo,
                                   'fecha': fecha,
                                   'cod_postal': codigo_postal}
    print()


def no_atendidos_fecha(peticiones_solicitud, atenciones):
    no_atendidos = []
    fecha = str(input("Introduce la fecha(yyyy-mm-dd): "))
    for num_correlativo, peticion_solicitud in peticiones_solicitud.items():
        if num_correlativo not in atenciones:
            if peticion_solicitud['fecha'] == fecha:
                no_atendidos.append(peticion_solicitud)
    num_no_atendidos = str(len(no_atendidos))
    print("No han sido atendidas "+num_no_atendidos+" peticiones del dia "+fecha)
    print()


def numero_ventas_fecha(atenciones):
    atenciones_fecha = []
    fecha = str(input("Introduce la fecha(yyyy-mm-dd): "))
    for atencion in atenciones.values():
        if atencion['fecha'] == fecha:
            if atencion['tipo'] == 'venta' or atencion['tipo'] == 'Venta' or atencion['tipo'] == 'V' or atencion['tipo'] == 'v':
                atenciones_fecha.append(atencion)
    num_atenciones_fecha = str(len(atenciones_fecha))
    print("Se han realizado "+num_atenciones_fecha+" ventas el dia "+fecha)
    print()


def numero_atendidos_codigo_postal(atenciones):
    atenciones_cod_postal = []
    cod_postal = int(input("Introduce el codigo postal: "))
    for atencion in atenciones.values():
        if atencion['cod_postal'] == cod_postal:
            atenciones_cod_postal.append(atencion)
    num_atenciones_cod_postal = str(len(atenciones_cod_postal))
    print("Se han atendido "+num_atenciones_cod_postal +
          " por el codigo postal "+str(cod_postal))
    print()


while True:
    print('Menu')
    print("Pulsa el numero de la operacion que desea realizar:")
    print("1 - Ingresar una peticion de atencion")
    print("2 - Registrar una atencion a un cliente")
    print("3 - ¿Cuantos no han sido atendidos en una fecha?")
    print("4 - Nº de ventas en una fecha concreta")
    print("5 - Nº de atendidos por codigo postal")
    print("6 - Guardar atenciones y peticiones")
    print("7 - Importar atenciones y peticiones de archivo")
    print("8 - Cerrar")
    operacion = int(input("Numero: "))

    if operacion == 1:
        registrar_numero_peticion_atencion(peticiones_solicitud)
    elif operacion == 2:
        registrar_atencion_cliente(peticiones_solicitud, atenciones)
    elif operacion == 3:
        no_atendidos_fecha(peticiones_solicitud, atenciones)
    elif operacion == 4:
        numero_ventas_fecha(atenciones)
    elif operacion == 5:
        numero_atendidos_codigo_postal(atenciones)
    elif operacion == 6:
        lg.guardar_datos(peticiones_solicitud, atenciones)
    elif operacion == 7:
        datos = lg.leer_datos()
        peticiones_solicitud = datos['peticiones']
        atenciones = datos['atenciones']
    elif operacion == 8:
        print("Cerrando...")
        exit()
