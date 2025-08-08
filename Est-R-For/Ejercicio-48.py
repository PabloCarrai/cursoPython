"""  
Realizar un programa que lea los lados de n triangulo.
Informar 
a) de cada uno de ellos, que tipo de triangulo es
(equilatero(tres lados iguales),Isosceles(dos lados iguales
escaleno(ningun lado igual)))
b) Cantidad de triangulos de cada tipo
"""

cTequilateros = 0
cTisosceles = 0
cTescaleno = 0
cTaCargar = int(input("Cuantos triangulos va a cargar?   "))
for e in range(cTaCargar):
    lado = int(input("Ingrese Primer Lado "))
    lado1 = int(input("Ingrese Segundo Lado "))
    lado2 = int(input("Ingrese Tercer Lado "))
    if ((lado != lado1) and (lado1 != lado2) and (lado != lado2)):
        print("Escaleno")
        cTescaleno = cTescaleno+1
    else:
        if ((lado == lado1) and (lado == lado2) and (lado1 == lado2)):
            print("Equilatero")
            cTequilateros = cTequilateros+1
        else:
            print("Isosceles")
            cTisosceles = cTisosceles+1
print("Triangulos Escaleno")
print(cTescaleno)
print("Triangulos Equilatero")
print(cTequilateros)
print("Triangulos Isosceles")
print(cTisosceles)
