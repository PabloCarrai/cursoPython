""" 
Confeccionar un programa que genere un numero aleatorio entre 1 y 100 y no se muestre. 
El operador debe tratar de adivinar el numero ingresado. 
Cada vez que ingrese un numero mostrar un mensaje "Gano" si es igual al generado o
"El numero aleatorio es mayor" o "El numero aleatorio es menor"
Mostrar cuando gana el jugador cuantos intentos necesito. 
"""
import random


aleatorio = random.randint(1, 100)


def jugar(aleatorio):
    contador = 0
    gano = 0
    while gano == 0:
        sueleccion = int(input(f"Adivine el numero  "))
        if (sueleccion == aleatorio):
            print(f"Gano el numero es {aleatorio}")
            print(f"Intentos {contador}")
            gano = 1
        else:
            if (sueleccion > aleatorio):
                print("El numero aleatorio es menor")
                contador += 1
            else:
                if (sueleccion < aleatorio):
                    print("El numero aleatorio es mayor")
                    contador += 1


jugar(aleatorio)
