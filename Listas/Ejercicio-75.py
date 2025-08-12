""" 
Una empresa tiene dos turnos(mañana y tarde)
en los que trabajan 8 empleados(4 mañana y 4 tarde)
Confeccionar un programa que permita almacenar los sueldos
de los empleados agrupados en dos lista. 
Imprimir las dos listas de sueldos
"""

#   Lista sueldos turno mañana
sueldosEmpleadostM = []
#   Lista sueldos turno noche
sueldosEmpleadostN = []
for i in range(4):
    #   pido ambos sueldos por vez
    sueldo = float(input("Sueldo empleado turno Mañana  "))
    sueldo1 = float(input("Sueldo empleado turno Tarde  "))
    #   Los agrego a las listas
    sueldosEmpleadostM.append(sueldo)
    sueldosEmpleadostN.append(sueldo1)

print("Sueldos de ambos turnos")
for i in range(4):
    print(sueldosEmpleadostM[i])
    print(sueldosEmpleadostN[i])
