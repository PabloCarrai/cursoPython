"""    
Confeccionar un programa que lea n pares de datos.
Cada par de datos corresponde a la medida de la 
base y la altura de un triangulo. El programa debera
informar. 
a) De cada triangulo la medida de su base,
su altura y su superficie
b) La cantidad de triangulos cuya superficie
sea mayor a 12
"""

CtSMayorDoce = 0
cValoresCargar = int(input("Ingrese cuantos triangulos va a cargar  "))
for i in range(cValoresCargar):
    base = int(input("Ingrese la base del triangulo "))
    altura = int(input("Ingrese la altura del triangulo "))
    superficie = (base*altura)/2
    print(f"Base-{base}, Altura-{altura} Superficie-{superficie}")
    if superficie > 12:
        print("Superficie mayor 12")
        CtSMayorDoce = CtSMayorDoce+1
print(f"Cantidad de triangulos con superficie mayor a 12: {CtSMayorDoce}")
