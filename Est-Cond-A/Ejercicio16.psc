// Se ingresa por teclado un valor entero.
// Mostrar una leyenda que indique si el numero
// es positivo, negativo o nulo.
Algoritmo Ejercicio16
	Escribir 'Ingrese un numero'
	Leer numero
	Si numero>0 Entonces
		Escribir 'Numero Positivo'
		Escribir numero
	SiNo
		Si numero<0 Entonces
			Escribir 'Numero Negativo'
			Escribir numero
		SiNo
			Escribir 'Numero Neutro'
			Escribir numero
		FinSi
	FinSi
FinAlgoritmo
