// Un postulante a un empleo.
// Realiza un test de capacitacion.
// Se obtuvo la siguiente informacion
// Cantidad total de preguntas que
// se le realizaron y cantidad de preguntas
// que contesto correctamente. Se pide confeccionar
// un programa que ingrese los datos por teclado
// e informe el nivel del mismo segun
// el porcentaje de respuestas correctas
// que ha obtenido y sabiendo que
// Nivel Maximo Porcentaje>=90
// Nivel Medio Porcentaje>=75 y <90
// Nivel Regular Porcentaje>=50 y <75
// Fuera de nivel Porcentaje <=50
Algoritmo Ejercicio18
	Escribir 'Ingrese cantidad de preguntas '
	Leer ctpreguntas
	Escribir 'Ingrese cantidad de preguntas respondidas correctamente'
	Leer cprespondidas
	porcentaje <- cprespondidas*100/ctpreguntas
	Si porcentaje>=90 Entonces
		Escribir 'Nivel Maximo'
		Escribir porcentaje
	SiNo
		Si porcentaje>=75 Entonces
			Escribir 'Nivel Medio'
			Escribir porcentaje
		SiNo
			Si porcentaje>=50 Entonces
				Escribir 'Nivel Regular'
				Escribir porcentaje
			SiNo
				Escribir 'Fuera de nivel'
				Escribir porcentaje
			FinSi
		FinSi
	FinSi
FinAlgoritmo
