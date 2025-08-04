""" 
Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete
mostrar el mensaje Promocionado/a
"""
nota = int(input("Ingrese Primer Nota "))
nota1 = int(input("Ingrese Segunda Nota "))
nota2 = int(input("Ingrese Tercer Nota "))
promedio = (nota+nota1+nota2)/3
if (promedio >= 7):
    print("Promocionado/a")
