// Confeccionar un programa que lea tres numeros enteros
// distintos y nos muestre el mayor
Algoritmo Ejercicio19
	Escribir 'Ingrese Primer Numero'
	Leer numero
	Escribir 'Ingrese Segundo Numero'
	Leer numero1
	Escribir 'Ingrese Tercer Numero'
	Leer numero2
	Si numero>numero1 Y numero>numero2 Entonces
		Escribir 'El mayor es '
		Escribir numero
	SiNo
		Si numero1>numero2 Entonces
			Escribir 'El mayor es '
			Escribir numero1
		SiNo
			Escribir 'El mayor es '
			Escribir numero2
		FinSi
	FinSi
FinAlgoritmo
