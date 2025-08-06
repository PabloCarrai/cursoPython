""" 
De un operario se conoce su sueldo y los años de antiguedad. 
Se pide confeccionar un programa que lea los datos de entrada
e informar.
a)Si el sueldo es inferior a 500 y su antiguedad 
es igual o superior a 10 años. Otorgarle un aumento 
del 20%, mostrar el sueldo a pagar. 

b)Si el sueldo esinferior a 500 pero su antiguedad 
es menor a 10 años otorgarle un aumento de 5%

c)Si el sueldo es mayor o igual a 500 mostrar 
el sueldo en pantalla sin cambios. 
"""
sueldo = int(input("Ingrese el sueldo del empleado "))
ant = int(input("Ingrese la antiguedad del empleado "))
print("El sueldo seria")
if (sueldo < 500 and ant >= 10):
    sueldo = sueldo*1.20
    print(sueldo)
else:
    if (sueldo < 500 and ant < 10):
        sueldo = sueldo*1.05
        print(sueldo)
    else:
        if (sueldo >= 500):
            print(sueldo)
