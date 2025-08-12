"""  
Crear y cargar una lista con 5 enteros por teclado. 
Implementar un algoritmo que identifique el 
menor valor de la lista y la posicion en donde se encuentra
"""

listaValores = []

#   Cargamos la lista
for p in range(5):
    valor = int(input("Valor?  "))
    listaValores.append(valor)

posicionMenor = 0
#   Supongo que el primer elemento es el menor
menor = listaValores[0]
#   Compruebo eso
for p in range(5):
    if (listaValores[p] < menor):
        menor = listaValores[p]
        posicionMenor = p

print("Lista completa ")
print(listaValores)
print("Menor ")
print(menor)
print("Posicion en la lista")
print(posicionMenor)
