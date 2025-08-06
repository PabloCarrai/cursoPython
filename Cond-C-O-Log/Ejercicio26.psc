// De un operario se conoce su sueldo y los años de antiguedad.
// Se pide confeccionar un programa que lea los datos de entrada
// e informar.
// a)Si el sueldo es inferior a 500 y su antiguedad
// es igual o superior a 10 años. Otorgarle un aumento
// del 20 MOD , mostrar el sueldo a pagar.
// b)Si el sueldo es inferior a 500 pero su antiguedad
// es menor a 10 años otorgarle un aumento de 5 MOD
// c)Si el sueldo es mayor o igual a 500 mostrar
// el sueldo en pantalla sin cambios.
Algoritmo Ejercicio26
	Escribir 'Ingrese el sueldo del empleado '
	Leer sueldo
	Escribir 'Ingrese la antiguedad '
	Leer antiguedad
	Si sueldo<500 Y antiguedad>=10 Entonces
		sueldo <- sueldo*1.20
		Escribir 'El sueldo seria '
		Escribir sueldo
	SiNo
		Si sueldo<500 Y antiguedad<10 Entonces
			sueldo <- sueldo*1.05
			Escribir 'El sueldo seria '
			Escribir sueldo
		SiNo
			Si sueldo>=500 Entonces
				Escribir 'El sueldo seria '
				Escribir sueldo
			FinSi
		FinSi
	FinSi
FinAlgoritmo
