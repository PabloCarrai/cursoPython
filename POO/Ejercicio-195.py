"""  
Conreccionar una clase que administre una agenda personal.
Se debe almacenar el nombre de la persona, telefono y mail. 
Debe mostrar un menu con las siguientes opciones. 
1) Carga de un contacto de la agenda. 
2) Listado completo de la agenda. 
3) Consulta ingresando el nombre de la persona
4) Modificacion de su telefono y mail
5) Finalizar el programa
"""


class Agenda():
    def __init__(self):
        self.agenda = {}
        self.menu()

    def menu(self):
        opcion = "s"
        while opcion not in (1, 2, 3, 4, 5):
            menu = """
            1) Carga de Contacto 
            2) Listado de la Agenda. 
            3) Consulta Contacto
            4) Modificar Telefono y Mail
            5) Salir    
            """
            print(menu)
            opcion = int(input("Elija una opcion valida (1, 2, 3, 4, 5)  "))
            if opcion == 1:
                self.cargarContacto()
                self.menu()
            else:
                if opcion == 2:
                    self.listadoContacto()
                    self.menu()
                else:
                    if opcion == 3:
                        self.consultaContacto()
                        self.menu()
                    else:
                        if opcion == 4:
                            self.modificarContacto()
                            self.menu()
                        else:
                            if opcion == 5:
                                self.salir()

    def cargarContacto(self):
        nombre = input("Nombre del contacto?  ")
        telefono = input("Telefono?  ")
        mail = input("Mail? ")
        self.agenda[nombre] = (telefono, mail)
        print(
            f"Contacto agregado Nombre:{nombre} Telefono: {telefono} Mail: {mail}")

    def listadoContacto(self):
        for i in self.agenda:
            print(
                f"Nombre: {i} Telefono: {self.agenda[i][0]} Mail:{self.agenda[i][1]}")

    def consultaContacto(self):
        contacto = input("Ingrese el nombre del contacto a consultar ")
        while contacto not in self.agenda:
            contacto = input("Ingrese un contacto valido ")
        print(
            f"Nombre: {contacto} Telefono: {self.agenda[contacto][0]} Mail:{self.agenda[contacto][1]}")

    def modificarContacto(self):
        self.listadoContacto()
        contacto = input("Que contacto desea modificar?  ")
        while contacto not in self.agenda:
            contacto = input("Ingrese un contacto valido de los existentes. ")
        telefono = input("Telefono?  ")
        mail = input("Mail? ")
        self.agenda[contacto] = (telefono, mail)

    def salir(self):
        print("Muchas gracias por usar esta aplicacion  ")


agenda = Agenda()
