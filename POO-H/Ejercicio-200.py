""" 
Ahora plantearemos otro problema empleando herencia. 
Supongamos que necesitamos implementar dos clases
que llamaremos Suma y Resta. Cada clase tiene como 
atributo valor1, valor2 y resultado. 
Los metodos a definir son carga1(que inicializa el atributo valor1)
carga2(que inicializa el atributo valor2) operar(que en el caso
de la clase Suma suma los dos atributos y en el caso de la 
clase resta hace la diferencia entre valor1 y valor2)
y otro metodo mostrar_resultado
Si analizamos ambas clases encontramos que muchos atributos
y metodos son identicos. En estos casos es bueno definir
una clase padre que agrupe dichos atributos y responsabilidades
comunes. 
La relacion de herencia que podemos disponer para este problema es:
    Operacion
Suma    Resta
Solamente el metodo operar es distintos para las clases suma y resta
(Esto hace que no lo podamos disponer en la clase Operacion en principio)
luego los metodos cargar1, cargar2 y mostrar_resultado son identicos a las
dos clases, esto hace que podamos disponerlo en la clase Operacion. 
Lo mismo los atributos valor1,valor2 y resultado se definiran en la clase
padre Operaciones
"""


class Operaciones:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1(self):
        self.valor1 = int(input("Valor? "))

    def cargar2(self):
        self.valor2 = int(input("valor? "))

    def mostrar_resultado(self):
        print(self.resultado)

    def operar(self):
        pass


class Suma(Operaciones):
    def operar(self):  # Sobrescribe Operar de la clase Operaciones
        self.resultado = self.valor1+self.valor2


class Resta(Operaciones):
    def operar(self):  # Sobrescribe Operar de la clase Operaciones
        self.resultado = self.valor1-self.valor2


suma1 = Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
suma1.mostrar_resultado()
resta1 = Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
resta1.mostrar_resultado()
