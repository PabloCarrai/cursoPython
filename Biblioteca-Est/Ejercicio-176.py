#   Importo el modulo random
import random

#   Uso la fundion randint de random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print(f"El dado 1 da {dado1}")
print(f"El dado 2 da {dado2}")

suma = dado1+dado2
if suma == 7:
    print("Gano")
else:
    print("Perdio")
