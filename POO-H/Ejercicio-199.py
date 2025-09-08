"""  
Plantear una clase Persona que contenga dos atributos:
nombre y edad. Definir como responsabilidades la carga
por teclado y su impresion. 
En el bloque principal del programa definir un objeto
de la clase persona y llamar a sus metodos. 
Declarar una segunda clase llamada Empleado que herede
de la clase Persona y agruege un atributo sueldo y 
muestre si debe pagar impuesto(sueldo superior a 3000)
Tambien en el bloque principal del programa crear un 
objeto de la clase Empleado. 
"""


class Persona:
    def __init__(self):
        self.nombre = input("Nombre? ")
        self.edad = int(input("Edad? "))

    def imprimir(self):
        print(f"Nombre:{self.nombre} Edad:{self.edad}")


class Empleado(Persona):

    def __init__(self):
        super().__init__()  # llamo al init de la clase padre
        # Aca agrego un atributo propio del hijo(Empleado)
        self.sueldo = float(input("Ingrese Sueldo "))

    def imprimir(self):
        super().imprimir()  # ejecuto el metodo imprimir de la clase padre
        # y agrego mi atributo de clase hijo
        print(f"Sueldo del empleado {self.sueldo}")

    def paga_impuesto(self):  # Este metodo es propio de Empleado
        if self.sueldo > 3000:
            print("Paga Impuesto")
        else:
            print("No paga Impuesto")


# juan = Persona()
# juan.imprimir()

empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuesto()
