"""  
Plantear una clase Rectangulo, definir dos
atributos(ladomenor y ladomayor). Redefinir
el operador == de tal forma que tenga en cuenta
la superficie del rectangolo. Lo mismo con todos
los otros operadores relacionales. 
"""


class Rectangulo:
    def __init__(self, ladomenor, ladomayor):
        self.ladomenor = ladomenor
        self.ladomayor = ladomayor

    def retornar_superficie(self):
        return self.ladomenor*self.ladomayor

    def __eq__(self, objeto2):
        if self.retornar_superficie() == objeto2.retornar_superficie():
            return True
        else:
            return False

    def __ne__(self, objeto2):
        if self.retornar_superficie() != objeto2.retornar_superficie():
            return True
        else:
            return False

    def __gt__(self, objeto2):
        if self.retornar_superficie() > objeto2.retornar_superficie():
            return True
        else:
            return False

    def __ge__(self, objeto2):
        if self.retornar_superficie() >= objeto2.retornar_superficie():
            return True
        else:
            return False

    def __lt__(self, objeto2):
        if self.retornar_superficie() < objeto2.retornar_superficie():
            return True
        else:
            return False

    def __le__(self, objeto2):
        if self.retornar_superficie() <= objeto2.retornar_superficie():
            return True
        else:
            return False


rectangulo1 = Rectangulo(1, 10)
rectangulo2 = Rectangulo(5, 20)

if rectangulo1 == rectangulo2:
    print("Rectangulo 1 es igual que Rectangulo2")
else:
    print("Restangulo 2 no es igual que Rectangulo 1")
