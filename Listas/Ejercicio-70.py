""" 
Definir una lista que almacene por asignacion los nombres de
5 personas. Contar cuantos de esos nombres tienen 5 o mas caracteres
"""
#   Necesito un contador
cantNombresMasCincoCaracteres = 0
#   La lista que usamos
nombres = ["Ana", "Eleonora", "Mariana", "Laura", "Juana",]
#   Recorremos por cantidad de elementos en la lista
for i in range(len(nombres)):
    #   Reviso que el nombre sea >=7
    if (len(nombres[i]) >= 5):
        #   Lo cuento
        cantNombresMasCincoCaracteres = cantNombresMasCincoCaracteres+1
print("Listado completo")
print(nombres)
#   Imprimimos
print("Cantidad de nombres de >=5 caracteres ")
print(cantNombresMasCincoCaracteres)
