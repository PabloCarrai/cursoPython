"""
Se tiene una lista con un conjunto de tuplas
con los nombres y las edades de personas.
personas = [("Pedro", 33), ("Ana", 3), ("Juan", 13), ("Carla", 45)]
Generar una lista con las personas mayores de edad
"""

personas = [("Pedro", 33), ("Ana", 3), ("Juan", 13), ("Carla", 45)]
personas_mayores=[per for per in personas if per[1]>=18]
print(personas)
print(personas_mayores)