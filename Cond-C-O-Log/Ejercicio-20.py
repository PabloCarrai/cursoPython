"""
Se carga una fecha(dia,mes y año) por teclado.
Mostrar un mensaje si corresponde al primer
trimestre del año(enero,febrero o marzo)
Cargar por teclado el valor numerico del dia
mes año ejemplo dia:10 mes:2 año:2020
"""
dia = int(input("Ingrese el dia "))
mes = int(input("Ingrese el mes "))
anio = int(input("Ingrese el año "))
if ((mes == 1) or (mes == 2) or (mes == 3)):
    print("Corresponde al primer trimestre")
