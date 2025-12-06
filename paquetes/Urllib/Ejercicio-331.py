from urllib import request

pagina = request.urlopen(
    "https://terli.wordpress.com/2022/07/30/pero-que-temazo-canten-putos/"
)
datos = pagina.read()
datosutf8=datos.decode("utf-8")
print(datosutf8)
