""" 
Escribir un programa que pida ingresar coordenadas(x,y)
que representan puntos en el plano. 
Informar cuantos puntos se han ingresado en el primero,
segundo, tercer y cuarto cuadrante. 
Al comenzar el programa se pide que se ingrese
cantidad de puntos a procesar. 
"""

acPrimerCuadrante = 0
acSegundoCuadrante = 0
acTercerCuadrante = 0
acCuartoCuadrante = 0
cPProcesar = int(input("Ingrese cantidad de puntos a procesar   "))
for l in range(cPProcesar):
    coordenadax = int(input("Ingrese coordenada X  "))
    coordenaday = int(input("Ingrese coordenada Y  "))
    if (coordenadax > 0 and coordenaday > 0):
        print("Priner Cuadrante")
        acPrimerCuadrante = acPrimerCuadrante+1
    else:
        if (coordenadax < 0 and coordenaday > 0):
            print("Segundo Cuadrante")
            acSegundoCuadrante = acSegundoCuadrante+1
        else:
            if (coordenadax < 0 and coordenaday < 0):
                print("Tercer Cuadrante")
                acTercerCuadrante = acTercerCuadrante+1
            else:
                if (coordenadax > 0 and coordenaday < 0):
                    print("Cuarto Cuadrante")
                    acCuartoCuadrante = acCuartoCuadrante+1

print("Cantidad Primer Cuadrante")
print(acPrimerCuadrante)
print("Cantidad Segundo Cuadrante")
print(acSegundoCuadrante)
print("Cantidad Tercer Cuadrante")
print(acTercerCuadrante)
print("Cantidad Cuarto Cuadrante")
print(acCuartoCuadrante)
