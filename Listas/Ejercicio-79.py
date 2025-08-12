""" 
Cargar una lista con 5 elementos enteros. 
Imprimir el mayor y un mensaje si se repite
dentro de la lista(es decir si dicho valor
se encuentra en 2 o mas posiciones en la lista)
"""

#   Cuento cuantas veces aparece el mayor en la lista
seRepite = 0
#   Creo la lista en donde guardare los valores
lista = []
#   Cargo los valores en la lista
for i in range(5):
    valor = int(input("Valor?   "))
    lista.append(valor)
#   Hago el tema de obtener el valor mayor
mayor = lista[0]
for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
#   Reviso cuantas veces aparece el mayor en la lista
for i in range(len(lista)):
    if lista[i] == mayor:
        seRepite = seRepite+1
#   Si se repite mas de 1 vez tengo que avisar
if (seRepite > 1):
    print("Se repite ")
    print(seRepite)
    print("Veces")

print("Lista completa ")
print(lista)
#   Imprimo el mayor
print("Mayor ")
print(mayor)
