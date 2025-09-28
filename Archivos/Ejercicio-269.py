archivo = open("/home/ed/cursoPython/datos.txt", "r")
lineas = archivo.readlines()
archivo.close()
print(f"cantidad de lineas {len(lineas)}")
for linea in lineas:
    print(linea)
