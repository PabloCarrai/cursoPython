// Escribir un programa en el cual dada una lista de tres valores
// numericos distintos se calcule e informe su rango de variacion
// (mostrar el mayor y el menor)
Algoritmo Ejercicio27
	Escribir 'Ingrese Primer numero '
	Leer numero
	Escribir 'Ingrese Segundo numero '
	Leer numero1
	Escribir 'Ingrese Tercer numero '
	Leer numero2
	maximo <- 0
	minimo <- 0
	Si ((numero>numero1) Y (numero>numero2)) Entonces
		maximo <- numero
	SiNo
		Si ((numero1>numero) Y (numero1>numero2)) Entonces
			maximo <- numero1
		SiNo
			Si ((numero2>numero) Y (numero2>numero1)) Entonces
				maximo <- numero2
			FinSi
		FinSi
	FinSi
	Si ((numero<numero1) Y (numero<numero2)) Entonces
		minimo <- numero
	SiNo
		Si ((numero1<numero) Y (numero1<numero2)) Entonces
			minimo <- numero1
		SiNo
			Si ((numero2<numero) Y (numero2<numero1)) Entonces
				minimo <- numero2
			FinSi
		FinSi
	FinSi
	Escribir 'Naximo'
	Escribir maximo
	Escribir 'Minimo'
	Escribir minimo
FinAlgoritmo
