"""
Confeccionar una funcion que reciba un string
como parametro y en forma opcional
un segundo string con un caracter. La funcion
debe mostrar el string subrayado con el
caracter que indica el segundo parametro
"""


def titulo_subrayado(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Sistema de Ventas", "_")
