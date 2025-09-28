archivo = open("/home/ed/cursoPython/datos.txt", "r")
for linea in archivo:
    print(linea, end="")
archivo.close()
