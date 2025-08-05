""" 
Escribir un programa que pida ingresar la coordenada de un
punto en el plano, es decir dos valores enteros 
x e y(distinto a cero).Posteriormente imprimir en pantalla
en que cuadrante se ubica dicho punto
y>0 x>0 1 cuadrante
y>0 x<0 2 cuadrante
y<0 x<0 3 cuadrante
y<0 x>0 4 cuadrante
"""
cy = int(input("Ingrese coordenada de y "))
cx = int(input("Ingrese coordenadas de x "))
if ((cy > 0) and (cx > 0)):
    print("Primer Cuadrante ")
else:
    if ((cy > 0) and (cx < 0)):
        print("Segundo Cuadrante")
    else:
        if ((cy < 0) and (cx < 0)):
            print("Tercer cuadrante")
        else:
            if ((cy < 0) and (cx > 0)):
                print("Cuarto cuadrante")
            else:
                print("Se encuentra sobre un eje")
