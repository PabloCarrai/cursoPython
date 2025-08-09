"""  
Realizar la carga de enteros por teclado.
Preguntar despues que ingresa el valor 
si desea cargar otro valor debiendo el 
operador ingresar la cadena "si" o "no"
por teclado. Mostrar la suma de los valores
ingresados
"""
#   Aca sumarizamos los valores
acumulador = 0
#   auxiliar para salir o seguir el programa
aux = "si"
#   mientras aux sea igual a "si"
while aux == "si":
    #   pedimos un valor
    valor = int(input("Ingrese un valor   "))
    #   Agregamos el valor cargado al acumulador
    acumulador = acumulador+valor
    #   confirmamos si quiere continuar cargando valores
    continuar = input("Desea continuar (si-no)  ")
    #   si elije si continuamos sino sobrescribimos la variable aux con no
    if (continuar == "si"):
        aux = "si"
    else:
        aux = "no"
#   Imprimimos lo sumarizado
print("Acumulamos ")
print(acumulador)
