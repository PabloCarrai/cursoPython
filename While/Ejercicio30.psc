// Desarrollar un programa que permita la carga
// de 10 valores por teclado y nos muestre
// posteriormente la suma de los valores
// ingresados y su promedio
Algoritmo Ejercicio30
	x <- 1
	suma <- 0
	Mientras x<=10 Hacer
		Escribir 'Ingrese un valor'
		Leer valor
		suma <- suma+valor
		x <- x+1
	FinMientras
	promedio <- suma/10
	Escribir 'La suma es '
	Escribir suma
	Escribir 'El promedio es '
	Escribir promedio
FinAlgoritmo
