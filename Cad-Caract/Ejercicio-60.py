""" 
Ingresar un correo por teclado. 
Verificar si el string ingresado
contiene un caracter @
"""
aux = 0
mail = input("Ingresa un correo ")
for x in range(len(mail)):
    if (mail[x] == "@"):
        aux = 1
if aux == 1:
    print("El mail ingresado contiene un caracter @")
else:
    print("El mail ingresado no contiene un caracter @")
