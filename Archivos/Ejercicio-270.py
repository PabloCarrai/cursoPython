#   Abrimos para añadir elementos al archivo
archivo = open("/home/ed/cursoPython/datos.txt", "a")
#   Agregamos contenido
archivo.write("Nueva Linea \n")
archivo.write("Nueva Linea \n")
archivo.write("Nueva Linea \n")
#   Cierro el archivo
archivo.close()
#   Ahora lo abrimos para leer
archivo = open("/home/ed/cursoPython/datos.txt", "r")
#   Leo su contenido
contenido = archivo.read()
#   Cierro el archivo
archivo.close()
#   Muestro el contenido
print(contenido)
