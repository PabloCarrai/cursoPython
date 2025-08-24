def retornar_superficie(lado):
    sup = lado*lado
    #   Con return devolvemos un valor en la funcion
    return sup


la = int(input("Lado del cuadrado?  "))
superficie = retornar_superficie(la)
print("Superficie del cuadrado es ")
print(superficie)
