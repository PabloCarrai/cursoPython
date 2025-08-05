"""
Un postulante a un empleo.
Realiza un test de capacitacion.
Se obtuvo la siguiente informacion
Cantidad total de preguntas que
se le realizaron y cantidad de preguntas
que contesto correctamente. Se pide confeccionar
un programa que ingrese los datos por teclado
e informe el nivel del mismo segun
el porcentaje de respuestas correctas
que ha obtenido y sabiendo que
Nivel Maximo Porcentaje>=90
Nivel Medio Porcentaje>=75 y <90
Nivel Regular Porcentaje>=50 y <75
Fuera de nivel Porcentaje <=50
"""
ctpreguntas = int(input("Ingrese cantidad total de preguntas "))
crpreguntas = int(input("Ingrese cantidad de preguntas respondidas "))
porcentaje = crpreguntas*100/ctpreguntas
if (porcentaje >= 90):
    print("Nivel Maximo")
    print(porcentaje)
else:
    if (porcentaje >= 75):
        print("Nivel Medio")
        print(porcentaje)
    else:
        if (porcentaje >= 50):
            print("Nivel Regular")
            print(porcentaje)
        else:
            print("Fuera de Nivel")
            print(porcentaje)
