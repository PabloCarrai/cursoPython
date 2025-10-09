while True:
    #   Intento pedir numeros
    try:
        valor1 = int(input("Valor? "))
        valor2 = int(input("Valor) "))
        division = valor1 / valor2
        print(f"La division da {division}")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    respuesta = input("Quiere seguir cargando valores s/n?")
    if respuesta == "n":
        break
