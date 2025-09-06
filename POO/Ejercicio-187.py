""" 
Confeccionar una clase que permita carga el nombre y la edad
de una persona. Mostrar los datos cargados. Imprimir un mensaje
si es mayor de edad(edad>=18)
"""


class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad}")

    def mayorEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad ya que tiene {self.edad} años")
        else:
            print(f"{self.nombre} no es mayor de edad ya que tiene {self.edad} años")


#   Esto lo hago asi para sacar un bucle que cargue los datos a lo pavo
nombres_variables = ["persona", "persona1", "persona2"]
nombres = ["juana", "miguel", "Lautaro"]
edades = [18, 17, 19]


""" 
Esto dedicado al puto profesor de programacion orientada a objeto
del curso en el ... . Me mareaba siempre con esta mierda de generar
muchos objetos a lo pavo y siempre quedaba mareado. En tu cara Libertario
"""

for i in range(len(nombres_variables)):
    nombres_variables[i] = Persona()
    nombres_variables[i].inicializar(nombres[i], edades[i])
    nombres_variables[i].mostrar()
    nombres_variables[i].mayorEdad()

# persona = Persona()
# persona.inicializar("Juana", 18)
# persona.mostrar()
# persona.mayorEdad()

# persona1 = Persona()
# persona1.inicializar("Juancito", 10)
# persona1.mostrar()
# persona1.mayorEdad()
