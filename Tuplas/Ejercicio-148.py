"""  
Definir una serie de listas y
tuplas anidadas
"""


empleado = ["ana", 45, (1, 2, 2020)]
print(empleado)
empleado.append((1, 5, 2020))
print(empleado)

#   Aca solo me deja modificar lo que haya en la lista
alumno = ("Juan", [8, 5])
print(alumno)
alumno[1].append(10)
print(alumno)
