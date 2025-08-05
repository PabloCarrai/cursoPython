"""
Se ingresan por teclado tres numeros.
Si alguno de los valores ingresados son
menores a 10, imprimir en pantalla
la leyenda. "Alguno de los numeros son menores a Diez"
"""

numero = int(input("Ingrese Primer Numero  "))
numero1 = int(input("Ingrese Segundo Numero  "))
numero2 = int(input("Ingrese Tercer Numero  "))
if ((numero < 10) or (numero1 < 10) or (numero2 < 10)):
    print("Alguno de los numeros son menores a Diez(10)")
