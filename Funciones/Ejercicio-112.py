def mostrar_mensaje(mensaje):
    print("-------------------------------------------------------")
    print(mensaje)
    print("-------------------------------------------------------")


def carga_suma():
    valor = int(input("Valor? "))
    valor1 = int(input("Valor? "))
    print(valor+valor1)


mostrar_mensaje(
    "El programa calculo el valor de la suma de dos valores por teclado")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")
