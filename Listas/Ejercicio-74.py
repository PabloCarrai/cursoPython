""" 
Cargar por teclado y almacenar en una lista
las alturas de 5 personas.
Obtener el promedio de las mismas. 
Contar cuantas personas son mas altas que el promedio
y cuantas mas bajas
"""
#   Contador de alturas mayores al promedio
cantAlturaMayorPromedio = 0
#   Contador de alturas menores al promedio
contAlturaMenorPromedio = 0
#   Contador de alturas
contAlturas = 0
#   Lista con las alturas
alturas = []
#   Genero un ciclo para cargar las alturas
for i in range(5):
    altura = float(input("Altura?   "))
    #   Agrego a la lista
    alturas.append(altura)
    #   Sumo la altura al contador
    contAlturas = contAlturas+altura

#   Genero promedio
promedioAlturas = contAlturas/5

for i in range(5):
    if (alturas[i] > promedioAlturas):
        cantAlturaMayorPromedio = cantAlturaMayorPromedio+1
    else:
        if (alturas[i] < promedioAlturas):
            contAlturaMenorPromedio = contAlturaMenorPromedio+1

print("Promedio de alturas ")
print(promedioAlturas)
print("Cantidad de personas cuya altura sea Mayor al promedio  ")
print(cantAlturaMayorPromedio)
print("Cantidad de personas cuya altura sea Menor al promedio  ")
print(contAlturaMenorPromedio)
