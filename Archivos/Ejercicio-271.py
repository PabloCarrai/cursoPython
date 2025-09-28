#   Abrimos para leer y agregar datos
archivo = open("/home/ed/cursoPython/datos.txt", "r+")

#   Leemos el archivo
contenido = archivo.read()
#   Imprimimos el contenido
print(contenido)

#   Agregamos una linea
archivo.write("Ultima linea \n")

#   Leemos el archivo
contenido = archivo.read()
#   Imprimimos el contenido
print(contenido)
#   Cerramos el archivo
archivo.close()
