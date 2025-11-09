def operar(v1, v2, fn):
    return fn(v1, v2)


resultado = operar(10, 4, lambda x1, x2: x1 + x2)
print(resultado)

resultado1 = operar(10, 20, lambda x1, x2: x1 - x2)
print(resultado1)

resultado2 = operar(5, 4, lambda x1, x2: x1 * x2)
print(resultado2)
