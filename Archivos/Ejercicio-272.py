#   Abrimos creando el archivo con codificacion utf-8
archivo = open("/home/ed/cursoPython/datos.txt", "w", encoding="utf-8")

archivo.write("Linea 1\n")
archivo.write("Linea 2\n")
archivo.write("Linea 3\n")
archivo.write("🐴\n")
archivo.close()
