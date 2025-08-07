// Una planta que fabrica perfiles de hierro
// posee un lote de n piezas.
// Confeccionar un programa que pida
// ingresar por teclado la cantidad de
// piezas a procesar y luego ingrese la
// longitud de cada perfil. Sabiendo que
// la pieza cuya longitud este comprendida
// en el rango de 1.20 y 1.30 son aptas.
// Imprimir por pantalla la cantidad de
// piezas aptas que hay en el lote
Algoritmo Ejercicio31
	x <- 1
	cantidad <- 0
	Escribir 'Cuantas piezas va a cargar? '
	Leer cpiezas
	Mientras x<=cpiezas Hacer
		Escribir 'Cargue la longitud de la pieza'
		Leer largo
		x <- x+1
		Si largo>=1.20 Y largo<=1.30 Entonces
			cantidad <- cantidad+1
		FinSi
	FinMientras
	Escribir 'Cantidad de piezas aptas '
	Escribir cantidad
FinAlgoritmo
