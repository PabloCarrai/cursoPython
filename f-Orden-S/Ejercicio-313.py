"""
Definir una funcion de orden superior llamada operar.
Llengan como parametros dos enteros y una funcion.
En el bloque de la funcion llamar a la funcion que llega
como parametro y enviar las dos primeros parametros
la funcion retorna un entero.
"""


def operar(v1, v2, fn):
    return fn(v1, v2)


def sumar(v1, v2):
    return v1 + v2


def restar(v1, v2):
    return v1 - v2


def multiplicar(v1, v2):
    return v1 * v2


def dividir(v1, v2):
    if v2 == 0:
        print("No se puede dividir por 0")
    else:
        return v1 / v2


resultado = operar(10, 4, sumar)
print(resultado)

resultado1=operar(20,5,restar)
print(resultado1)

resultado2=operar(30,5,multiplicar)
print(resultado2)

