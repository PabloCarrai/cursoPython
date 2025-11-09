def imprimir_si(lista, fn):
    for elemento in lista:
        if fn(elemento):
            print(elemento)


lista = [9, 20, 70, 60, 19]

print("Valores pares ")
imprimir_si(lista, lambda x: x % 2 == 0)

print("Multiplos de 3 y 5")
imprimir_si(lista, lambda x: x % 3 == 0 or x % 5 == 0)


print("Mayores iguales a 50")
imprimir_si(lista, lambda x: x >= 50)

print("Valores entre 1 y 50 o entre 70 y 100")
imprimir_si(lista, lambda x: (x > 0 and x <= 50) or (x >= 70 and x <= 100))
