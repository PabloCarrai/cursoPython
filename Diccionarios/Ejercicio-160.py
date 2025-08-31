"""  
Crear un diccionario en python que defina como clave
el numero de documento de una persona. y como valor
un string con su nombre
Desarrollar las siguientes funciones. 
1) Cargar por teclado los datos de 4 personas. 
2) Listado completo del diccionario
3) Consulta del nombre de una persona ingresando
su numero de documento
"""


def cargar_datos():
    personas = {}
    for i in range(4):
        dni = int(input("DNI?  "))
        nombre = input("Nombre?  ")
        personas[dni] = nombre
    return personas


def mostrar_datos(personas):
    print("-"*60)
    print("Datos del Diccionario ")
    print("-"*60)
    for dni in personas:
        print(f"DNI: {dni}- Nombre: {personas[dni]}")
    print("-"*60)


def mostrar_consulta_dni(personas):
    print("-"*60)
    print("Consulta por dni ")
    print("-"*60)
    dni = int(input("DNI a consultar?  "))
    if dni in personas:
        print(f"DNI: {dni}- Nombre: {personas[dni]}")
    else:
        print(f"No tenemos registro de ninguna persona con ese DNI: {dni}")
    print("-"*60)


personas = cargar_datos()
mostrar_datos(personas)
mostrar_consulta_dni(personas)
