// Se ingresan un conjunto de n alturas dr personas por teclado.
// Mostrar la altura promedio de las personas.
Algoritmo Ejercicio33
	tAlturas <- 0
	x <- 1
	Escribir 'Cuantas alturas va a ingresar?'
	Leer cIngresos
	Mientras x<=cIngresos Hacer
		x <- x+1
		Escribir 'Ingrese la altura'
		Leer altura
		tAlturas <- tAlturas+altura
	FinMientras
	promedio <- tAlturas/cIngresos
	Escribir 'El promedio de las alturas es '
	Escribir promedio
FinAlgoritmo
