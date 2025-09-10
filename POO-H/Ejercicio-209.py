"""  
Crear una clase Persona que tenga como 
atributo el nombre y la edad. 
El operador == retornara verdadero su las dos
personas tienen la misma edad, el operador >
retornara True si la edad del objeto de la 
izquierda tiene una edad mayor a la edad
del objeto de la derecha del operador > y asi
sucesivamente. 
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, objeto2):
        if self.edad == objeto2.edad:
            return True
        else:
            return False

    def __ne__(self, objeto2):
        if self.edad != objeto2.edad:
            return True
        else:
            return False

    def __gt__(self, objeto2):
        if self.edad > objeto2.edad:
            return True
        else:
            return False

    def __ge__(self, objeto2):
        if self.edad >= objeto2.edad:
            return True
        else:
            return False

    def __lt__(self, objeto2):
        if self.edad < objeto2.edad:
            return True
        else:
            return False

    def __le__(self, objeto2):
        if self.edad <= objeto2.edad:
            return True
        else:
            return False


persona1 = Persona("Ana", 1)
persona2 = Persona("Yesica", 18)

# if persona1 == persona2:
#     print("Iguales")
# else:
#     print("Nada que ver")

# if persona1 != persona2:
#     print("Son distintos")
# else:
#     print("Son iguales")

# if persona1 > persona2:
#     print("Es mayor")
# else:
#     print("No es mayor")

# if persona1 < persona2:
#     print("Es menor")
# else:
#     print("No es menor")

if persona1 <= persona2:
    print(f"{persona1.nombre} Es menor/igual a {persona2.nombre}")
else:
    print("No es menor/igual")
