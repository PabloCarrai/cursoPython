""" 
Confeccionar un programa que permita. 
1) Cargar una lista de 10 enteros. 
2) Generar dos listas a partir de la primer. En una
guardar los valores positivos, y en la otra los negativos. 
3) Imprimir las dos listas generadas
"""


def cargarDiezElementos():  # 1
    lista = []
    for i in range(10):
        valores = int(input("Valor? "))
        lista.append(valores)
    return lista


def separarElementosPositivosNegativos(lista):  # 2
    positivos = []
    negativos = []
    for i in range(len(lista)):
        if (lista[i] > 0):
            positivos.append(lista[i])
        else:
            if (lista[i] < 0):
                negativos.append(lista[i])
    return positivos, negativos


def inprimirListas(lista):  # 3
    for i in range(len(lista)):
        print("Valores ")
        print(f"{lista[i]}")


listaPura = cargarDiezElementos()
positivos, negativos = separarElementosPositivosNegativos(listaPura)
print("Positivos")
inprimirListas(positivos)
print("Negativos")
inprimirListas(negativos)
