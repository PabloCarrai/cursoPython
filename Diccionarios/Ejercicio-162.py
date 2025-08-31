"""
Confeccionar una agenda. Utilizar un diccionario
cuya clave sea la fecha. Permitir almacenar
distintas avtividades en una misma fecha(se
ingrese la hora y la actividad)
Implementar las siguientes funciones
1)  Carga de datos en la agenda.
2)  Listado completo de la agenda
3)  Consulta de una fecha.

Para entender si se cargara por asignacion
tendriamos una estructura de datos similar a
la siguiente.

agenda = {"1/5/2020": [("10:00", "correr"), ("12:00", "almorzar"), ("22:00", "cenar")],
          "1/5/2020": [("8:00", "ginnasia"), ("10:30", "reunion de trabajo")]}

"""


def cargar_datos():
    agenda = {}
    # Cuantas fechas va a cargar
    cfechasCargar = int(input("Cuantas fechas pienza cargar a la agenda?   "))
    for x in range(cfechasCargar):
        # Esta es la clave del diccionario
        fecha = input("Ingrese la fecha del evento  ")
        ceventosporfecha = int(
            input(f"Cuantos eventos tiene el dia {fecha}  "))
        listaDia = []  # Auxiliar en donde meto todo lo de un dia en particular
        for i in range(ceventosporfecha):
            horario = input("Horario?  ")  # Esto es la hora del evento
            evento = input("Evento?  ")  # Esto es el evento en si
            listaDia.append((horario, evento))
        agenda[fecha] = listaDia
    return agenda


def listar_agenda(agenda):
    for fecha in agenda:
        print(f"Eventos para la fecha {fecha}  ")
        for i in range(len(agenda[fecha])):
            # Como me cuesta esto. LPTM
            print(f"{agenda[fecha][i][0]},{agenda[fecha][i][1]}")


def listar_agenda_Fecha(agenda):
    fecha = input("Fecha que quiere consultar?  ")
    if fecha in agenda:
        print(f"Eventos para la fecha {fecha}  ")
        for i in range(len(agenda[fecha])):
            # Como me cuesta esto. LPTM
            print(f"{agenda[fecha][i][0]},{agenda[fecha][i][1]}")
    else:
        print(f"No hay eventos para esa fecha {fecha}  ")
    pass


agenda = cargar_datos()
listar_agenda(agenda)
listar_agenda_Fecha(agenda)
