"""
Definir una lista con 5 valores enteros.
Mostrar los 5 valores formateados a derecha
junto a su suma.
"""

lista = [2000, 500, 17000, 7]
for elemento in lista:
    print(f"{elemento:10}")  # Esto :10 separa a la derecha 10 espacio(por lo que veo)
print("-------------------")
print(f"{sum(lista):10}")
