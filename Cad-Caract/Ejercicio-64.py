""" 
Solicitar el ingreso de una clave por teclado. 
Almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga 
entre 10 y 20 caracteres para que sea valido. 
Caso contrario mostrar mensaje de error. 
"""

clave = input("Ingrese una clave    ")
if len(clave) >= 10 and len(clave) <= 20:
    print("Clave Valida ")
else:
    print("Clave invalida(pocos caracteres)")
