// Realizar un programa que permita cargar dos listas
// de 15 valores cada una. Informar con un mensaje
// cual de las dos listas tiene un valor acumulado mayor.
// Lista 1 mayor Lista 2 Mayor Listas iguales
Algoritmo Ejercicio37
	acumuladorListaUno <- 0
	acumuladorListaDos <- 0
	aux <- 1
	Mientras aux<=15 Hacer
		aux <- aux+1
		Escribir 'Ingresar Valor Lista 1'
		Leer valor
		acumuladorListaUno <- acumuladorListaUno+valor
	FinMientras
	aux <- 1
	Mientras aux<=15 Hacer
		aux <- aux+1
		Escribir 'Ingresar Valor Lista 2'
		Leer valor
		acumuladorListaDos <- acumuladorListaDos+valor
	FinMientras
	Si acumuladorListaUno=acumuladorListaDos Entonces
		Escribir 'Listas Iguales'
	SiNo
		Si acumuladorListaUno>acumuladorListaDos Entonces
			Escribir 'Lista 1 Mayor'
		SiNo
			Escribir 'Lista 2 Mayor'
		FinSi
	FinSi
FinAlgoritmo
