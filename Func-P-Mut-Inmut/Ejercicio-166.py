""" 
Confeccionar un programa que almacene en un diccionario
como clave el nombre de un contacto y como valor su numero
telefonico. 
1) Carga de contacto y su numero telefonico
2) Permitir modificar el numero telefonico. Se ingresa el nombre
del contacto para su busqueda
3) Imprimir la lista completa de contactos con sus numeros telefonicos
"""


def cargar_contacto():
    contactos = {}
    continuamos = "s"
    print("-"*60)
    while continuamos == "s":
        print("Ingreso de contactos ")
        nombre = input("Nombre?  ")
        telefono = input("Telefono?  ")
        contactos[nombre] = telefono
        continuamos = input("Quiere cargar otro contacto s/n? ")
    print("-"*60)
    return contactos


def editar_contacto(diccionario):
    print("-"*60)
    nombre = input("Contacto a buscar?  ")
    print("-"*60)
    if nombre in diccionario:
        nuevoTelefono = input(f"Ingrese el nuevo numero de {nombre} ")
        diccionario[nombre] = nuevoTelefono
        print("Modificacion realizada")
    else:
        print("Contacto no existente ")
    print("-"*60)


def mostrar_contactos(diccionario):
    print("-"*60)
    print("Contactos existentes  ")
    for elemento in diccionario:
        print(f"Contacto: {elemento} Telefono: {diccionario[elemento]}")
    print("-"*60)


contactos = cargar_contacto()
mostrar_contactos(contactos)
editar_contacto(contactos)
mostrar_contactos(contactos)
