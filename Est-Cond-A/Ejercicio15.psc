// Se cargan por teclado tres numeros distintos
// Mostrar por pantalla el mayor de ellos
Algoritmo Ejercicio15
	Escribir 'Ingrese Primer Numero'
	Leer numero
	Escribir 'Ingrese Segundo Numero'
	Leer numero1
	Escribir 'Ingrese Tercer Numero'
	Leer numero2
	Si numero>numero1 Entonces
		Si numero>numero2 Entonces
			Escribir 'El mayor es '
			Escribir numero
		FinSi
	FinSi
	Si numero1>numero Entonces
		Si numero1>numero2 Entonces
			Escribir 'El mayor es '
			Escribir numero1
		FinSi
	FinSi
	Si numero2>numero Entonces
		Si numero2>numero1 Entonces
			Escribir 'El mayor es '
			Escribir numero2
		FinSi
	FinSi
FinAlgoritmo
