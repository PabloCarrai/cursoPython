class Cliente:
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def __add__(self, objeto2):
        suma = self.monto+objeto2.monto
        return suma


cliente1 = Cliente("Ana", 1200)
cliente2 = Cliente("Juan", 1000)
print("Suma total de ambos clientes")
print(cliente1+cliente2)
