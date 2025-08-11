"""  
Definir por asignacion una lista de 8
elementos enteros. Contar cuantos de dichos
valores almacenan un valor superior a 100
"""
#   Defino un contador
contadorValoresMayoresCien = 0
#   Definimos por asignacion una lista con 8 valores
valores = [101, 198, 45, 26, 35, 77, 151, 130]
#   Recorro la lista usando indices con la cantidad de elementos de la lista
for x in range(len(valores)):
    #   Chequeo si hay algun valor mayor a 100
    if valores[x] > 100:
        #   Aumento en 1 para el caso que se cumpla la condicion
        contadorValoresMayoresCien = contadorValoresMayoresCien+1
print("Cantidad de elementos mayores a 100  ")
#   Imprimo la cantidad de valores encontrados que cumplan la condicion
print(contadorValoresMayoresCien)
