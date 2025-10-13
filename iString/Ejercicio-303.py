"""
Definir una lista con 5 valores flotantes
con distintas cantidades de decimales.
Mostrar los numeros solo con dos
decimales
"""

lista = [20.00, 500.45, 17000.567, 7.5456]
for elemento in lista:
    print(
        #    Aca solo muestro dos decimales(10 es los espacio a la derecha .2f es los decimales)
        f"{elemento:10.2f}"
    )
