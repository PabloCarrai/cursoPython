""" 
Elaborar una funcion que muestre la tabla de multiplicar del valor que enviemos como parametro. 
Definir un segundo parametro llamado termino que por defecto almacene el valor 10. Se debera
mostrar tantos terminos de la tabla de multiplicar como lo indica el segundo parametro. 
Llamar a la funcion desde el bloque principal de nuestro programa con argumentos nombrados
"""


def tablaMultiplicar(valorTabla, parametros=10):
    print("-"*40)
    print(f"Tabla de multiplicar del {valorTabla} hasta el {parametros}")
    print("-"*40)
    for i in range(1, parametros):
        print(f"{i}*{valorTabla}={i*valorTabla}")
    print("-"*40)


tablaMultiplicar(3, 14)
tablaMultiplicar(3)
tablaMultiplicar(valorTabla=44, parametros=39)
