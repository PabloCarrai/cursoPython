"""
Confeccionar una funcion que reciba tres enteros
y los muestre ordenados de menor a mayor. En otra
funcion solicitar la carga de 3 enteros por teclado y
proceder a llamar a la primer funcion definida.
"""


def ordenarEnteros(v, v1, v2):
    valorMaximo = 0
    #   No lo pide pero vemos si hay algun valor igual
    if ((v == v1) or (v1 == v2) or (v2 == v)):
        print("Valores iguales. ")
        obtenerTresEnteros()
    else:
        #   Primer Valor Mayor?
        if ((v > v1) and (v > v2)):
            valorMaximo = v
        else:
            #   Segundo Valor Maximo?
            if ((v1 > v) and (v1 > v2)):
                valorMaximo = v1
            else:
                #   Tercer Valor Maximo?
                if ((v2 > v) and (v2 > v1)):
                    valorMaximo = v2

    valorMinimo = 0
    #   Primer Valor Menor?
    if ((v < v1) and (v < v2)):
        valorMinimo = v
    else:
        #   Segundo Valor Menor?
        if ((v1 < v) and (v1 < v2)):
            valorMinimo = v1
        else:
            #   Tercer Valor Menor?
            if ((v2 < v) and (v2 < v1)):
                valorMinimo = v2
    #   Sumo el maximo y el minimo y lo resto al valor de los tres enteros obteniendo el medio
    valorMedio = (v+v1+v2)-(valorMaximo+valorMinimo)

    print("Minimo")
    print(valorMinimo)
    print("Medio")
    print(valorMedio)
    print("Maximo")
    print(valorMaximo)


def obtenerTresEnteros():
    print("Ingrese los tres valores ")
    v = int(input("Primer Valor?   "))
    v1 = int(input("Segundo Valor?   "))
    v2 = int(input("Tercer Valor?   "))
    ordenarEnteros(v, v1, v2)


obtenerTresEnteros()
