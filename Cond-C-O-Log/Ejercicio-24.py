"""  
Se ingresan tres valores por teclado
Si todos son iguales se imprime la 
suma del primer con el segundo
y a este se lo multiplica por el tercero
"""
numero = int(input("Ingrese Primer Numero  "))
numero1 = int(input("Ingrese Segundo Numero  "))
numero2 = int(input("Ingrese Tercer Numero  "))
suma = numero+numero1
multi = suma*numero2
if ((numero == numero1) and (numero == numero2)):
    print("Todos iguales")
    print("La suma es ")
    print(suma)
    print("La suma multiplicado por el tercero es")
    print(multi)
