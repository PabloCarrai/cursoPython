#   Lista con componente listas
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(lista)
#   Imprimir primer componente
print(lista[0])
#   Primer componente primer indice
print(lista[0][0])
#   Usando for para imprimir, solo primer componente de la lista[0]
for i in range(len(lista[0])):
    print(lista[0][i])
#   Imprimimos cada lista y cada elemento de la misma
for i in range(len(lista)):
    for x in range(len(lista[i])):
        print(lista[i][x])
