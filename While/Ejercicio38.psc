// Desarrollar un programa que permita
// cargar n numeros enteros y luego
// nos informe cuantos valores fueron
// pares y cuantos inpares.
// Emplear el operador  MOD  en la condicion
Algoritmo Ejercicio38
	AcNumerosPar <- 0
	AcNumerosInPar <- 0
	aux <- 1
	Escribir 'Cuantos numeros va a cargar?'
	Leer cNCargar
	Mientras aux<=cNCargar Hacer
		Escribir 'Ingrese un valor '
		Leer valor
		aux <- aux+1
		Si valor MOD 2==0 Entonces
			Escribir 'Numero Par'
			AcNumerosPar <- AcNumerosPar+1
		SiNo
			Escribir 'Numero InPar'
			AcNumerosInPar <- AcNumerosInPar+1
		FinSi
	FinMientras
	Escribir 'Cantidad de numeros Pares'
	Escribir AcNumerosPar
	Escribir 'Cantidad de numeros InPares'
	Escribir AcNumerosInPar
FinAlgoritmo
