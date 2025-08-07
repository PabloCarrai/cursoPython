"""  
En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 500
Realizar un programa que lea los sueldos que cobra cada empleado e informar
cuantos empleados cobran entre 100 y 300 y cuantos cobran mas de 300. 
Ademas el programa debera informar el importe que gasta la empresa
en sueldos al personal
"""
AcumuladorSuedosCienTrescientos = 0
AcumuladorSueldosMasTrescientos = 0
ContadorSueldosCienTrescientos = 0
ContadorSueldoMasTrescientos = 0
aux = 1
CSueldosCargar = int(input("Cuantos Sueldos va a Cargar?"))
while (aux <= CSueldosCargar):
    sueldo = float(input("Ingrese el sueldo "))
    if (sueldo >= 100 and sueldo <= 300):
        #   Cuento cantidad de empleados cobran entre 100 y 300
        ContadorSueldosCienTrescientos = ContadorSueldosCienTrescientos+1
        #   Acumulo el total que cobran estos empleados
        AcumuladorSuedosCienTrescientos = AcumuladorSuedosCienTrescientos+sueldo
    else:
        if (sueldo > 300):
            #   Cuento cantidad de empleados con sueldo mayores a 300
            ContadorSueldoMasTrescientos = ContadorSueldoMasTrescientos+1
            #   Acumulo El total que cobran estos empleados
            AcumuladorSueldosMasTrescientos = AcumuladorSueldosMasTrescientos+sueldo
    #   Aumento el auxiliar para que el bucle no sea infinito
    aux = aux+1

#   El total de los sueldos que se pagan
totalSueldos = AcumuladorSuedosCienTrescientos+AcumuladorSueldosMasTrescientos
print("Cantidad de empleados con sueldos entre 100 y 300  ")
print(ContadorSueldosCienTrescientos)
print("Cantidad de empleados con sueldos mayores a 300")
print(ContadorSueldoMasTrescientos)
print("El total de los sueldos pagados es ")
print(totalSueldos)
