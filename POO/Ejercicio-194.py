"""

Plantear una clase que administre dos listas de 5
nombres de alumnos y sus notas. Mostrar un menu
de opciones que permita:
1) Cargar alumnos
2) Listar alumnos
3) Mostrar alumnos con notas mayores o iguales a 7
4) Finalizar el programa.
"""


class Estudiantes():
    def __init__(self):
        self.alumnos = []
        self.notas = []
        self.menu()

    def menu(self):
        opcion = "s"
        while opcion not in (1, 2, 3, 4):
            menu = """
            1) Cargar Alumnos:
            2) Listar Alumnos:
            3) Mostrar alumnos nota >= 7
            4) Finalizar        
            """
            print(menu)
            opcion = int(input("Elija una opcion valida 1,2,3,4  "))
        if opcion == 1:
            self.cargarAlumno()
            self.menu()
        else:
            if opcion == 2:
                self.listarAlumno()
                self.menu()
            else:
                if opcion == 3:
                    self.mostrarAlumno()
                    self.menu()
                else:
                    if opcion == 4:
                        self.salir()

    def cargarAlumno(self):
        continuamos = "s"
        while continuamos == "s":
            alumno = input("Alumno? ")
            nota = int(input("Nota? "))
            self.alumnos.append(alumno)
            self.notas.append(nota)
            continuamos = input("Continuamos s/n?")

    def listarAlumno(self):
        for e in range(len(self.alumnos)):
            print(f"Alumno {self.alumnos[e]} Nota: {self.notas[e]}")

    def mostrarAlumno(self):
        print("Alumnos notas >= 7  ")
        for e in range(len(self.alumnos)):
            if self.notas[e] >= 7:
                print(f"Alumno {self.alumnos[e]} Nota: {self.notas[e]}")

    def salir(self):
        print("Gracias por usar el programa")


estudiante = Estudiantes()
