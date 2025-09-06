"""
Implementar una clase llamada Alumno que tenga
como atributos su nombre, y su nota. Definir los metodos
para inicializar sus atributos, imprimirlos y mostrar
un mensaje si esta regular(nota mayor o igual a 4)
Definir dos objetos de la clase Alumno
"""


class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"El alumno se llama {self.nombre}, su nota es {self.nota}")

    def mostrar(self):
        if self.nota >= 4:
            print(f"Alumno: {self.nombre} Nota: {self.nota} Estado: Regular")
        else:
            print(f"Alumno: {self.nombre} Nota: {self.nota} Estado: Libre")


pedro = Alumno()
pedro.inicializar("Pedro", 5)
pedro.imprimir()
pedro.mostrar()

daniel = Alumno()
daniel.inicializar("Daniel", 2)
daniel.imprimir()
daniel.mostrar()
