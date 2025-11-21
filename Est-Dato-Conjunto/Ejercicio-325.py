"""
Definor dos conjuntos que almacenen cada uno
una serie de lenguajes de programacion.
Efectuar las cuatro operaciones basicas
con dichos conjuntos
"""

lenguajes1 = {"C", "Pascal", "PHP", "Python"}
lenguajes2 = {"C++", "Java", "Python"}

print(f"Lenguajes Estructurados {lenguajes1}")
print(f"Lenguajes orientados a Objetos {lenguajes2}")


# conjunto1 = lenguajes1 | lenguajes2
# print("Todos los lenguajes (Union)")
# print(conjunto1)
# conjunto2 = lenguajes1 & lenguajes2
# print("Interseccion de los dos conjuntos de lenguajes (Interseccion)")
# print(conjunto2)
# conjunto3 = lenguajes1 - lenguajes2
# print("Diferencia de los dos conjuntos de lenguajes (Diferencia)")
# print(conjunto3)
# conjunto4 = lenguajes1 ^ lenguajes2
# print("Lenguajes del conjunto1 o del conjunto2 pero no en ambos (Diferencia Simetrica)")
# print(conjunto4)

# Ahora usando los metodos y no tanto los operadores
# conjunto1 = lenguajes1.union(lenguajes2)
# print("Todos los lenguajes (Union)")
# print(conjunto1)
# conjunto2 = lenguajes1.intersection(lenguajes2)
# print("Interseccion de los dos conjuntos de lenguajes (Interseccion)")
# print(conjunto2)
# conjunto3 = lenguajes1.difference(lenguajes2)
# print("Diferencia de los dos conjuntos de lenguajes (Diferencia)")
# print(conjunto3)
# conjunto4 = lenguajes1.symmetric_difference(lenguajes2)
# print("Lenguajes del conjunto1 o del conjunto2 pero no en ambos (Diferencia Simetrica)")
# print(conjunto4)

#   Conjuntos disjuntos
dias_semana = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}
dias_feriados = {"sabado", "domingo"}
dias_laborables = {"lunes", "martes", "miercoles", "jueves", "viernes"}
# if dias_laborables.isdisjoint(dias_feriados):
#     print("Dias laborables no tiene elementos en comun con dias feriados")

#   igualdad de conjuntos,subconjuntos y superconjuntos

if dias_feriados < dias_semana:
    print("dias_feriados es un subconjunto de dias_semana")
if dias_feriados != dias_laborables:
    print("dias_feriados es distinto a dias_laborables")
if dias_semana > dias_laborables:
    print("dias_semana es un superconjunto de dias_laborables")
