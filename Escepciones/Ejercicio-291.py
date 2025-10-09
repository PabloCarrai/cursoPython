""" 
Capturar todas las exepciones sin discriminar el tipo. 
"""

while True:
    #   Intento pedir numeros
    try:
        valor1 = int(input("Valor? "))
        valor2 = int(input("Valor) "))
        division = valor1 / valor2
        print(f"La division da {division}")
    except: #Esto captura todas las exepciones
        print("problemas en el ingreso de datos")
    respuesta = input("Quiere seguir cargando valores s/n?")
    if respuesta == "n":
        break