def cargar():
    lista = []
    for i in range(5):
        valor = int(input("Valor?  "))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return (f"El mayor de la lista es: {mayor}")


def imprimir_suma(lista):
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    return f"El total es {total}"
