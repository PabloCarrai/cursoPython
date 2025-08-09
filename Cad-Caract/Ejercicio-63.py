""" 
Ingresar una oracion que puede tener letras
tanto en mayusculas como minusculas. 
Contar la cantidad de vocales. 
Crear un segundo string con toda la oracion en 
minuscula para que sea mas facil disponer la 
condicion que verifica que es una vocal
"""
acumuladorVocales = 0
oracion = input("Ingrese una oracion ").lower()
for i in range(len(oracion)):
    if (oracion[i] == "a" or oracion[i] == "e" or oracion[i] == "i" or oracion[i] == "o" or oracion[i] == "u"):
        acumuladorVocales = acumuladorVocales+1

print("Cantidad de vocales en la oracion ")
print(oracion)
print(acumuladorVocales)
