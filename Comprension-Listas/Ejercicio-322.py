"""
Se tiene una lista de nombres de personas
nombres = ["Juan", "Pablo", "Luis", "Mauro", "Hector"]
Generar otra lista cuyos elementos sean a su vez lista con
dos nombres de cada uno. Tener en cuenta que nunca se debe
combinar el mismo nombre dos veces
"""

nombres = ["Juan", "Pablo", "Luis", "Mauro", "Hector"]
nombres_compuestos = [[nombre1,nombre2] for nombre1 in nombres for nombre2 in nombres if nombre1!=nombre2]
# for nombres1 in nombres:
#     for nombre2 in nombres:
#         if nombres1 != nombre2:
#             nombres_compuestos.append([nombres1, nombre2])

print(nombres)
print(nombres_compuestos)
