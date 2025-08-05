// Se carga una fecha(dia,mes y año) por teclado.
// Mostrar un mensaje si corresponde al primer
// trimestre del año(enero,febrero o marzo)
// Cargar por teclado el valor numerico del dia
// mes año ejemplo dia:10 mes:2 año:2020
Algoritmo Ejercicio20
	Escribir 'Ingrese el dia'
	Leer dia
	Escribir 'Ingrese el mes'
	Leer mes
	Escribir 'Ingrese el año'
	Leer anio
	Si ((mes=1) O (mes=2) O (mes=3)) Entonces
		Escribir 'Corresponde al prime trimestre'
	FinSi
FinAlgoritmo
