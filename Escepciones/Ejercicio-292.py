try:
    archivo1 = open("datos.txt", "w")
    archivo1.write("Linea 1\n")
    archivo1.write("Linea 2\n")
    archivo1.write("Linea 3\n")
    archivo1.write(100)  #   Aca va a dar error siempre
except TypeError:
    print("No se puede grabar un entero con el write")
finally:
    archivo1.close()  #   Eso si o si se tiene que ejecutar no podemos dejar abierto el archivo
    print(f"Se cerro el archivo")