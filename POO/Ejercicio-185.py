""" 
Implementaremos una clase llamada Persona que tendra
como atributo(variable) su nombre y dos metodos(funciones)
uno de dichos metodos inicializara el atributo nombre y 
el siguiente metodo mostrara en pantalla el contenido del mismo
Definir dos objetos de la clase Persona
"""


class Persona:  # Definicion de la clase Persona
    #   metodos
    def inicializar(self, nombre):
        #   referencia al atributo
        self.nombre = nombre

    def imprimir(self):
        print(f"Nombre {self.nombre}")


#   Creacion de un objeto persona
persona1 = Persona()
persona1.inicializar("Pedro")
persona1.imprimir()


persona2 = Persona()
persona2.inicializar("Ana")
persona2.imprimir()
