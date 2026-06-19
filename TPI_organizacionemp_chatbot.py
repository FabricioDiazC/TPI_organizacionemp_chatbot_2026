#Trabajo Practico Integrador - Organizacion Empresarial - UTN 
import os
import csv

ARCHIVO_EMPLEADOS = "empleados.csv"
ARCHIVO_SOLICITUDES = "solicitudes.csv"

#Simulacion de Base de Datos
def inicializar_archivos():
    #Crea los archivos CSV si no existen
    if not os.path.exists(ARCHIVO_EMPLEADOS):
        with open(ARCHIVO_EMPLEADOS, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["legajo", "nombre", "dias_disponibles"])
            escritor.writerow(["1001", "Juan Perez", "14"])
            escritor.writerow(["1002", "Ana Gomez", "5"])
            escritor.writerow(["1003", "Carlos Diaz", "21"])

    if not os.path.exists(ARCHIVO_SOLICITUDES):
        with open(ARCHIVO_SOLICITUDES, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["legajo", "dias_solicitados", "estado"])


#Busca un empleado por legajo en el CSV
def buscar_empleado(legajo):
    with open(ARCHIVO_EMPLEADOS, mode="r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila["legajo"] == legajo:
                return fila
    return None


def actualizar_saldo(legajo, nuevo_saldo):
    #Reescribe el CSV de empleados actualizando el saldo de un legajo puntual.
    filas = []
    with open(ARCHIVO_EMPLEADOS, mode="r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        campos = lector.fieldnames
        for fila in lector:
            if fila["legajo"] == legajo:
                fila["dias_disponibles"] = str(nuevo_saldo)
            filas.append(fila)

    with open(ARCHIVO_EMPLEADOS, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)


def registrar_solicitud(legajo, dias, estado):
    #Agrega una nueva fila al historial de solicitudes
    with open(ARCHIVO_SOLICITUDES, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([legajo, dias, estado])


# MAQUINA DE ESTADOS DEL BOT
# Estados posibles: INICIO, PEDIR_LEGAJO, PEDIR_DIAS, CONFIRMAR, FIN

def ejecutar_bot():
    estado = "INICIO"
    legajo_actual = None
    empleado_actual = None

    print("Bot de Gestion de Vacaciones")

    while estado != "FIN":
        match estado:

            case "INICIO":
                print("\nBienvenido. Escriba 'salir' en cualquier momento para cancelar.")
                estado = "PEDIR_LEGAJO"

            case "PEDIR_LEGAJO": 
                entrada = input("Ingrese su numero de legajo: ").strip()

                if entrada.lower() == "salir":
                    print("Operacion cancelada por el usuario.")
                    estado = "FIN"
                    continue

                #Camino Infeliz: validar que sea numerico
                if not entrada.isdigit():
                    print("Error: el legajo debe ser un valor numerico. Intente nuevamente.")
                    continue

                empleado_actual = buscar_empleado(entrada)

                if empleado_actual is None:
                    print("Error: legajo no encontrado en la base de datos. Verifique e intente de nuevo.")
                    continue  # se mantiene en PEDIR_LEGAJO

                legajo_actual = entrada
                print(f"Hola {empleado_actual['nombre']}. "
                      f"Su saldo disponible es de {empleado_actual['dias_disponibles']} dias.")
                estado = "PEDIR_DIAS"

            case "PEDIR_DIAS":
                entrada = input("¿Cuantos dias de vacaciones desea solicitar?: ").strip()

                if entrada.lower() == "salir":
                    print("Operacion cancelada por el usuario.")
                    estado = "FIN"
                    continue

                #Camino Infeliz: validar que sea numerico
                if not entrada.isdigit():
                    print("Error: debe ingresar un numero entero de dias. Intente nuevamente.")
                    continue

                dias_solicitados = int(entrada)
                saldo_actual = int(empleado_actual["dias_disponibles"])

                #Camino Infeliz: validar saldo
                if dias_solicitados <= 0:
                    print("Error: la cantidad de dias debe ser mayor a cero.")
                    continue

                if dias_solicitados > saldo_actual:
                    print(f"Su solicitud de {dias_solicitados} dias supera su saldo disponible "
                          f"({saldo_actual} dias).")
                    registrar_solicitud(legajo_actual, dias_solicitados, "Rechazada")
                    print("La solicitud fue registrada como RECHAZADA. "
                          "Puede intentar con una cantidad menor o salir.")
                    reintentar = input("¿Desea intentar con otra cantidad? (si/no): ").strip().lower()
                    if reintentar == "si":
                        continue  # vuelve a pedir dias
                    else:
                        estado = "FIN"
                        continue

                # Gateway de aprobacion automatica
                nuevo_saldo = saldo_actual - dias_solicitados
                actualizar_saldo(legajo_actual, nuevo_saldo)
                registrar_solicitud(legajo_actual, dias_solicitados, "Aprobada")

                print(f"Solicitud APROBADA. Se descontaron {dias_solicitados} dias. "
                      f"Nuevo saldo disponible: {nuevo_saldo} dias.")
                estado = "CONFIRMAR"

            case "CONFIRMAR":
                print("Su solicitud quedo registrada en el sistema")
                estado = "FIN"

            case _:
                print("Error: estado no reconocido. Reiniciando proceso.")
                estado = "INICIO"

    print("Terminando conversacion")



if __name__ == "__main__":
    inicializar_archivos()
    ejecutar_bot()