while True:
    #   Intento pedir numeros
    try:
        valor1 = int(input("Valor? "))
        valor2 = int(input("Valor) "))
        suma = valor1 + valor2
        print(f"La suma da {suma}")
    #   Si se equivoca y pone otro tipo de dato envio un mensaje
    except ValueError:  #    Evito con esto que el programa se detenga
        print("Debe ingresar numeros")
    respuesta = input("Quiere seguir cargando valores s/n?")
    if respuesta == "n":
        break
