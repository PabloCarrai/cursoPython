// Escribir un programa que solicite el ingreso de 10 notas
// de alumnos y nos informe cuantas tienen notas
// mayores o iguales a 7 y cuantas menores.
Algoritmo Ejercicio32
	nmayoresSiete <- 0
	nmenoresSiete <- 0
	x <- 1
	Mientras x<=10 Hacer
		x <- x+1
		Escribir 'Ingrese la nota '
		Leer nota
		Si nota>=7 Entonces
			nmayoresSiete <- nmayoresSiete+1
		SiNo
			nmenoresSiete <- nmenoresSiete+1
		FinSi
	FinMientras
	Escribir 'Cantidad de notas mayores/igual a 7'
	Escribir nmayoresSiete
	Escribir 'Cantidad de notas menores a 7'
	Escribir nmenoresSiete
FinAlgoritmo
