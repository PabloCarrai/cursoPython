"""  
Confeccionar un programa que pida por teclado tres notas de un alumno. 
Calcular el promedio e imprimir algunos de estos mensajes. 
Si el promedio es >=7 mostrar Promocionado
Si el promedio es >=4 y <7 mostrar Regular
Si el promedio es <4 mostrar Reprobado
"""

nota = int(input("Ingrese Primer Nota  "))
nota1 = int(input("Ingrese Segunda Nota  "))
nota2 = int(input("Ingrese Tercer Nota  "))
promedio = (nota+nota1+nota2)/3
if (promedio >= 7):
    print("Promocionado")
else:
    if (promedio >= 4):
        print("Regular")
    else:
        print("Reprobado")
