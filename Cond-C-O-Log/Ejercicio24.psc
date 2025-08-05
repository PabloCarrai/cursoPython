// Se ingresan tres valores por teclado
// Si todos son iguales se imprime la
// suma del primer con el segundo
// y a este se lo multiplica por el tercero
Algoritmo Ejercicio24
	Escribir 'Ingrese Primer Numero'
	Leer numero
	Escribir 'Ingrese Segundo Numero'
	Leer numero1
	Escribir 'Ingrese Tercer Numero'
	Leer numero2
	suma <- numero+numero1
	multi <- suma*numero2
	Si numero==numero1 Y numero==numero2 Entonces
		Escribir 'Todos iguales'
		Escribir 'La suma es '
		Escribir suma
		Escribir 'La suma multiplicado a numero3 es'
		Escribir multi
	FinSi
FinAlgoritmo
