// Realizar un programa que solicite la carga por teclado de dos numeros.
// Si el primero es mayor al segundo, informar su suma y diferencia.
// en caso contrario informar el producto y division del primero respecto al segundo
Algoritmo Ejercicio11
	Escribir 'Ingrese un numero'
	Leer numero
	Escribir 'Ingrese otro numero'
	Leer numero1
	suma <- numero+numero1
	dif <- numero-numero1
	prod <- numero*numero1
	div <- numero/numero1
	Si numero>numero1 Entonces
		Escribir 'La suma de ambos numeros es '
		Escribir suma
		Escribir 'La diferencia entre ambos es '
		Escribir dif
	SiNo
		Escribir 'El producto de ambos numeros es'
		Escribir prod
		Escribir 'La division entre ambos es '
		Escribir div
	FinSi
FinAlgoritmo
