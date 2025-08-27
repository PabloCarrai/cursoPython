"""  
Confeccionar una funcion que llegue como primer parametro
el nombre del empleado, como segundo parametro el costo por hora
y finalmente la cantidad de horas trabajadas. 
Llamar a dicha funcion empleando la caracteristica de python
de argumentos nombrados
"""


def calcular_Sueldo(nombre, costoporhora, cantidadhoras):
    sueldo = costoporhora * cantidadhoras
    print(nombre, " trabajo ", cantidadhoras, " y cobra ", sueldo)


calcular_Sueldo("ana", 10, 100)
calcular_Sueldo(cantidadhoras=50, nombre="Juan", costoporhora=45)
