archivo = open("/home/ed/cursoPython/datos.txt", "r")
contenidoLinea = archivo.readline()
print(contenidoLinea)
while contenidoLinea != "":
    print(contenidoLinea)
    contenidoLinea = archivo.readline()

archivo.close()
