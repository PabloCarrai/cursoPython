""" 
Confeccionar un programa que solicite la carga de 10 valores
por teclado. Mostrar al final su suma. Definir varias lineas
de comentarios indicando el nombre del programa
el programador y la fecha de la ultima modificacion
usar el # como comentario
"""

#   Programador: Pablo Carrai
#   Programa: Ejercicio-54.py
#   Ultima Mod: 9/8/25

#   Acumulador de la suma
acumulador = 0
for p in range(10):
    valor = int(input("Ingrese un valor "))  # Pedimos el valor por teclado
    acumulador = acumulador+valor  # Sumamos el valor cargado al contador
print("Totalizamos:")
print(acumulador)  # Mostramos el acumulado
