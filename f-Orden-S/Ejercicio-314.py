"""
Declarar una clase que almacene el nombre y la edad de una persona.
Definir un metodo que retorne True o False si la persona es mayor
de edad o no.
Este metodo debe recibir como parametro una funcion que al llamarla
pasando la edad de la persona retornara si es mayor o no de edad.
Tener en cuenta que una persona es mayor de edad en Estados unidos
si tiene 21 o mas años y en argentina si tiene 18 o mas años
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def esMayor(self, fn):
        return fn(self.edad)


def es_mayor_estadosUnidos(edad):
    if edad >= 21:
        return True
    else:
        return False


def es_mayor_argentina(edad):
    if edad >= 18:
        return True
    else:
        return False


daniel = Persona("Daniel", 23)
if daniel.esMayor(es_mayor_argentina):
    print(f"{daniel.nombre} tiene {daniel.edad} por lo tanto es mayor si vive en argentina")
else:
    print(f"{daniel.nombre} tiene {daniel.edad} por lo tanto no es mayor si vive en argentina")

juan = Persona("Juan", 17)
if juan.esMayor(es_mayor_estadosUnidos):
    print(f"{juan.nombre} tiene {juan.edad} por lo tanto es mayor si vive en estados unidos")
else:
    print(f"{juan.nombre} tiene {juan.edad} por lo tanto no es mayor si vive en estados unidos")
