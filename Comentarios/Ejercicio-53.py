"""   
Realizar un programa que solicite la carga
de valores enteros por teclado y los sume. 
Finalizar la carga al ingresar el valor -1.
Dejar comentario dentro del codigo fuente
el enunciado del problema y alguno otro 
comentario de linea pertinente
"""

#   Usamos un contador para sumar los valores
contador = 0
#   El auxiliar para poder manejar el flujo del while
aux = 1
#   usamos while para poder interrumpir
while aux == 1:
    valor = int(input("Ingrese un valor  "))
    contador = contador+valor
    if (valor == -1):
        aux = -1
        #   Para no restar el -1 posible usado en la salida del bucle
        contador = contador+1
print("Totalizamos ")
print(contador)
