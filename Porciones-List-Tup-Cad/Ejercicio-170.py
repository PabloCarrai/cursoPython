"""  
Confeccionar una funcion que reciba una cadena de caracteres y nos devuelva los tres primeros. 
En el bloque principal del programa a definir una tupla con los nombres de meses. Mostrar por 
pantalla los primeros tres caracteres de cada mes. 
"""


def devolver_tres_caracteres(palabra):
    for tres in palabra:
        print(tres[:3])


mes = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
       "agosto", "septiembre", "octubre", "noviembre", "diciembre")

devolver_tres_caracteres(mes)
