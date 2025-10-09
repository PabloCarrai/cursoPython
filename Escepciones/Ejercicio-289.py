"""
Almacenar en una tupla los nombres de los meses del año.
Solicitar el ingreso del numero del mes y mostrar
seguidamente el nombre de dicho mes. Captura la exepcion
indexerror
"""

meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)

try:
    nmeses=int(input("Ingrese un numero de mes entre 1 y 12  "))
    print(meses[nmeses-1])
except IndexError:
    print("El numero ingresado tiene que ser entre 1 y 12  ")
