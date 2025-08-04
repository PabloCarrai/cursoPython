"""  
Se ingresa por teclado un numero positivo de uno o dos digitos(1..99)
Mostrar un mensaje indicando si el numero tiene uno o dos digitos
"""
numero = int(input("Ingrese un numero "))
if numero > 9:
    print("El numero tiene dos digitos ")
else:
    print("El numero tiene un digito")
