""" 
Confeccionar una clase que represente un empleado. 
Definir como atributos su nombre y su sueldo. 
En el metodo __init__ cargar los atributos por teclado
y luego en otro metodo imprimir sus datos
y por ultimo uno que imprima un mensaje si debe
pagar impuesto(si el sueldo es superior a 3000)
"""


class Empleado:
    def __init__(self):  # al instanciar el objeto se llama solo
        self.nombre = input("Nombre? ")
        self.sueldo = float(input("Sueldo?  "))

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Sueldo: {self.sueldo}")

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuesto")
        else:
            print("No paga impuesto")


empleado = Empleado()
empleado.imprimir()
empleado.paga_impuestos()
