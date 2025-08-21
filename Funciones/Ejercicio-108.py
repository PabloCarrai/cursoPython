"""  
Confeccionar una aplicacion que muestre una presentacion en pantalla
del programa. Solicite la carga de dos valores ymuestre la suma. 
Mostrar finalmente un mensaje de despedida del programa. 
Implementar estas activiadades en tres funciones
"""

#   definimos una funcion


def presentacion():
    print("-------------------------------------------------------")
    print("Programa que permite cargar dos valores por teclado")
    print("Efectua la suma de los valores y muestra su resultado")
    print("-------------------------------------------------------")


def cargaSuma():
    valor = int(input("Valor?   "))
    valor1 = int(input("Valor?  "))
    print("La suma de ambos valores es ")
    print(valor+valor1)


def finalizacion():
    print("-------------------------------------------------------")
    print("Gracias por usar la aplicacion")
    print("-------------------------------------------------------")


#   Llamado a las funciones
presentacion()
cargaSuma()
finalizacion()
