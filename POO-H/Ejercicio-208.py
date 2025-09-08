"""   
Desarrollar una clase llamada Lista que permita
pasar al metodo __init__ una lista de valores
enteros. Redefinir los operadores + - * // 
a un valor entero
"""


class Lista:
    def __init__(self, valores=[]):
        self.valores = valores

    def imprimir(self):
        print(self.valores)

    def __add__(self, entero):
        nueva_lista = []
        for x in range(len(self.valores)):
            nueva_lista.append(self.valores[x]+entero)
        return nueva_lista

    def __sub__(self, entero):
        nueva_lista = []
        for x in range(len(self.valores)):
            nueva_lista.append(self.valores[x]-entero)
        return nueva_lista

    def __mul__(self, entero):
        nueva_lista = []
        for x in range(len(self.valores)):
            nueva_lista.append(self.valores[x]*entero)
        return nueva_lista

    def __floordiv__(self, entero):
        nueva_lista = []
        for x in range(len(self.valores)):
            nueva_lista.append(self.valores[x]//entero)
        return nueva_lista


lista = Lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lista.imprimir()
print(lista+5)
lista.imprimir()
print(lista-3)
lista.imprimir()
print(lista*4)
lista.imprimir()
print(lista//2)
