"""  
Confeccionar un programa que permita la carga
de una lista de 5 enteros por teclado. 
Luego en otra funcion
1) Imprimir en forma completa. 
2) Obtener y mostrar el mayor
3) Mostrar la suma de todas sus componentes
Utilizar la nueva sintais de for de la vista
en este componente
"""


def cargar():
    lista = []
    for x in range(5):
        num = int(input("Valor? "))
        lista.append(num)
    return lista


def imprimir(lista):
    print("Listado")
    #   nueva sintaxis del uso de for
    for elemento in lista:
        print(elemento)


def obtenerMayor(lista):
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    print("El mayor de la lista es ")
    print(mayor)


def sumarElementos(lista):
    suma = 0
    for elemento in lista:
        suma = suma+elemento
    print(f"La suma de todo da {suma}")


lista = cargar()
imprimir(lista)
obtenerMayor(lista)
sumarElementos(lista)
