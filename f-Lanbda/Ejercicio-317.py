def filtrar(cadena, fn):
    cad = ""
    for caracter in cadena:
        if fn(caracter):
            cad = cad + caracter
    return cad


cadena1 = "¿Esto es la prueba 1 o la prueba2?"
print("String original")
print(cadena1)
cadena2 = filtrar(
    cadena1,
    lambda car: car == "a"
    or car == "e"
    or car == "i"
    or car == "o"
    or car == "u"
    or car == "A"
    or car == "E"
    or car == "I"
    or car == "O"
    or car == "U",
)
print(cadena2)
cadena3 = filtrar(cadena1, lambda car: car >= "a" and car <= "z")
print(cadena3)
cadena4 = filtrar(
    cadena1,
    lambda car: not (car >= "a" and car <= "z") and not (car >= "A" and car <= "Z"))

print(cadena4)
