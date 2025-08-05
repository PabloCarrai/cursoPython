// Confeccionar un programa que permita
// cargar un numero entero positivo de hasta tres cifras
// y muestre un mensaje indicando si tiene 1,2 o 3 cifras.
// Mostrar un mensaje de error si el numero de cifras es mayor
Algoritmo Ejercicio17
	Escribir 'Ingrese un numero '
	Leer numero
	Si numero>999 Entonces
		Escribir 'Numero erroneo(Mas de 3 Cifras'
		Escribir numero
	SiNo
		Si numero>99 Entonces
			Escribir 'Es un numero de 3 cifras'
			Escribir numero
		SiNo
			Si numero>9 Entonces
				Escribir 'Numero de 2 Cifras'
				Escribir numero
			SiNo
				Escribir 'Numero de 1 Cifra'
				Escribir numero
			FinSi
		FinSi
	FinSi
FinAlgoritmo
