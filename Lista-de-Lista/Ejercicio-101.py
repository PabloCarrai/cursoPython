"""
Se desea saber la temperatura media trimestral de cuatro paises.
Para ello se tiene como dato las temperaturas medias mensuales de
dichos paises.
Se debe ingresar el nombre del pais y seguidamente las tres
temperatudas mensuales. Seleccionar la estructura de datos
adecuada para el almacenamiento de los datos en memoria.
a) Cargar por teclado los nombres de los paises
y las temperaturas medias mensuales.
b) Imprimir los nombres de los paises y las temperaturas
mensuales de las mismas.
c) calcular la temperatuda media trimestral de cada pais.
d) Imprimir los nombres de los paises y las temperaturas medias trimestrales.
e) Imprimir los nombres del pais con la temperatura media trimestral mayor
"""

paises = []
temperaturas = []
promediotemp = []

for elemento in range(4):
    pais = input("Pais? ")
    paises.append(pais)
    temperatura = int(input("Temperatura?  "))
    temperatura1 = int(input("Temperatura?  "))
    temperatura2 = int(input("Temperatura?  "))
    temperaturas.append([temperatura, temperatura1, temperatura2])
print("Pais y temperatura media ")
for x in range(4):
    print(paises[x], temperaturas[x][0],
          temperaturas[x][1], temperaturas[x][2])
for x in range(4):
    pro = (temperaturas[x][0]+temperaturas[x][1]+temperaturas[x][2])/3
    promediotemp.append(pro)
print("Promedio")
for x in range(4):
    print(paises[x], promediotemp[x])

posM = 0
for x in range(4):
    if (promediotemp[x] > promediotemp[posM]):
        posM = x
print("Mayora temperatura")
print(paises[posM])
