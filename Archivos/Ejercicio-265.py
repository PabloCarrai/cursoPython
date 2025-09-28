"""  
Crear un archivo de texto llamado datos.txt. Al macenar tres lineas de texto. 
Abrir luego el archivo creado con un editor de texto. 
"""

#   Abro el archivo datos.txt, si no existe lo crea
archivo = open("datos.txt", "w")
#   Escribo en el mismo
archivo.write("Primer Linea \n")
#   Escribo en el mismo
archivo.write("Segunda linea \n")
#   Escribo en el mismo
archivo.write("Tercer linea \n")
#   Escribo en el mismo
archivo.write("Cuarta linea \n")
#   Cierro el archivo
archivo.close()
print("Fin del programa")
