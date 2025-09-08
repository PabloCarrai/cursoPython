"""  
Definir una clase que almacene un codigo de cliente 
y un nombre. En la clase Cliente definir una variable
de clase de tipo lista que almacene todos los codigos
de clientes que tienen suspendidas sus cuentas corrientes
Imprimir por pantalla todos los datos de los clientes y 
el estado que se encuentra su cuenta corriente
"""


class Cliente:
    suspendidos = []  # Variable de Clase(tipo lista)

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def imprimir(self):
        print(f"Codigo: {self.codigo} Nombre: {self.nombre}")
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:  # para acceder es clase.variable
            print("Esta Suspendido")
        else:
            print("No esta suspendido")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


cliente1 = Cliente(1, "Carlos")
cliente2 = Cliente(2, "Ana")
cliente3 = Cliente(3, "Pedro")
cliente4 = Cliente(4, "Luis")

cliente2.suspender()
cliente3.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)
