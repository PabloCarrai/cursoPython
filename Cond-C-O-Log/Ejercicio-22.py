""" 
Se ingresan por teclado tres numeros. 
Si todos los valores ingresados son 
menores a 10, imprimir en pantalla
la leyenda. "Todos los numeros son menores a Diez"
"""
numero = int(input("Ingrese Primer Numero  "))
numero1 = int(input("Ingrese Segundo Numero  "))
numero2 = int(input("Ingrese Tercer Numero  "))
if ((numero < 10) and (numero1 < 10) and (numero2)):
    print("Son todos menores a 10")
