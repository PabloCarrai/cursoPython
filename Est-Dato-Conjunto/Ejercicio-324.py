conjunto1 = {1, 5, 10, 20}
print(conjunto1)
conjunto2 = {"Juan", 10, 6.4, True}
print(conjunto2)
conjunto3 = {("Juan", 10), (6.4, True)}
print(conjunto3)
lenguajes = {"C", "Pascal", "PHP", "Python"}
print(lenguajes)
lenguajes.add("Ruby")
print(lenguajes)
lenguajes.add("PHP")
print(lenguajes)
lenguajes1 = {"C", "Pascal", "PHP", "Python"}
print(lenguajes1)
lenguajes1.remove("Pascal")
print(lenguajes1)
lenguajes2 = {"C", "Pascal", "PHP", "Python"}
print(lenguajes2)
lenguajes2.discard("Pythones")
print(lenguajes2)
if "PHP" in lenguajes:
    print("PHP esta en el conjunto")
else:
    print("PHP no esta")
print(len(lenguajes))
lenguajes3 = set()
lenguajes3.add("C")
lenguajes3.add("PHP")
lenguajes3.add("Python")
lenguajes3.add("Pascal")
print(len(lenguajes3))
print(lenguajes3)
edades = [23, 21, 25, 21, 23]
print(edades)
conjunto = set(edades)
print(conjunto)

dias = {"lunes", "martes", "miercoles"}
for dia in dias:
    print(dia)
