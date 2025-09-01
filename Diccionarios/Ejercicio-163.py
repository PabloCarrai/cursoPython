""" 
Se desea almacenar los datos de 3 alumnos. 
Definir un diccionario cuya clave sea el numero
de documento del alumno. Como valor al macenar una
lista concomponentes del tipo tupla donde almacenan
nombre de materia y su nota. 
Crear la siguiente funciones. 
1) carga de los alumnos(de cada alumno solicitar
su dni y los nombres de las materias y sus notas.)
2) listado de todos los alumnos con sus notas. 
3) Consulta de un alumno por su dni, mostrar materias 
que cursa y sus notas. 

Si se cargara por asignacion tendria una estructura similar a 

alumnos = {1: [("programacion 1", 10), ("ingles 1", 7)], 2: [
    ("programacion", 7), 3("matematica", 4)]}


"""


def carga_alumnos():
    alumnos = {}
    continua = "s"
    while continua == "s":
        materias = []
        dni = input("DNI Del Estudiante?  ")
        continuaMateria = "s"
        while continuaMateria == "s":
            materia = input("Materia? ")
            nota = int(input("Nota? "))
            materias.append((materia, nota))
            continuaMateria = input("Necesita cargar otra materioa s/n? ")
        alumnos[dni] = materias
        continua = input("Desea continuar cargando Estudiantes?  ")
    return alumnos


def imprimir_alumnos(alumnos):
    for alumno in alumnos:
        print(f"DNI Del Alumno {alumno}")
        for materia, nota in alumnos[alumno]:
            print(f"Materia: {materia} Nota: {nota}")


def imprimir_alumno_dni(alumnos):
    dni = input("Ingrese DNI Del alumno a consultar  ")
    if dni in alumnos:
        for materia, nota in alumnos[dni]:
            print(f"Materia: {materia} Nota: {nota}")
    else:
        print(f"No se registran notas para un alumno con dicho dni {dni}")


alumnos = carga_alumnos()
imprimir_alumnos(alumnos)
imprimir_alumno_dni(alumnos)
