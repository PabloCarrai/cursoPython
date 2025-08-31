"""  
Desarrollar una aplicacion que nos permita
crear un diccionario en ingles/castellano. 
La clave es la palabra en ingles, y el valor
la palabra en castellano. 
Crear las siguientes funciones. 
1) cargar el diccionario
2) listado completo del diccionario
3) Ingresar por teclado una palabra en ingles
y si existe en el diccionadio mostrar su traduccion
"""


def cargar_diccionario():
    diccionario = {}
    cant_terminos = int(input("Cuantos elementos ingresara?   "))
    for i in range(cant_terminos):
        clave = input("Termino en Ingles?   ")
        valor = input("Su traduccion al español?  ")
        diccionario[clave] = valor
    return diccionario


def listar_diccionario(diccionario):
    print("El diccionario posee los siguientes terminos")
    for clave in diccionario:
        print(f"Ingles: {clave} Español: {diccionario[clave]}")


def mostrar_termino(diccionario):
    clave = input("Palabra en Ingles?   ")
    if clave in diccionario:
        print(f"La palabra {clave} se traduce como {diccionario[clave]}")
    else:
        print("No existe ese termino")


diccionario = cargar_diccionario()
listar_diccionario(diccionario)
mostrar_termino(diccionario)
