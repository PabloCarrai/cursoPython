""" 
Cargar una cadena por teclado. Luego:
1)  Imprimir los dos primeros caracteres
2)  Imprimir los dos ultimos caracteres
3)  Imprimir todos menos el primero y el ultimo
"""


def imprimir_Primeros_Dos(palabra):
    print(palabra[:2])


def imprimir_Ultimos_Dos(palabra):
    print(palabra[len(palabra)-2:])


def imprimir_Todo_Menos_Primer(palabra):
    print(palabra[1:len(palabra)-1])


palabra = input("Palabra?   ")
print(f"La palabra es {palabra}")
print("Dos Primeras letras de la palabra ")
imprimir_Primeros_Dos(palabra)
print("Ultimas dos letras de la palabra ")
imprimir_Ultimos_Dos(palabra)
print("Todas las letras menos la primera y ultima letra ")
imprimir_Todo_Menos_Primer(palabra)
