// Confeccionar un programa que pida por teclado tres notas de un alumno
// calcular el promedio e imprimir algunos de estos mensajes
// Si el promedio es >=7 mostrar "Promocionado"
// Si el promedio es >=4 y <7 mostrar "Regular"
// Si el promedio es <4 mostrar "Reprobado"
Algoritmo Ejercicio14
	Escribir 'Ingrese Primer Nota'
	Leer nota
	Escribir 'Ingrese Segunda Nota'
	Leer nota1
	Escribir 'Ingrese Tercer Nota'
	Leer nota2
	promedio <- (nota+nota1+nota2)/3
	Si promedio>=7 Entonces
		Escribir 'Promocionado'
	SiNo
		Si promedio>=4 Entonces
			Escribir 'Regular'
		SiNo
			Escribir 'Reprobado'
		FinSi
	FinSi
FinAlgoritmo
