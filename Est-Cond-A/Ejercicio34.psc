// En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 500
// Realizar un programa que lea los sueldos que cobra cada empleado e informar
// cuantos empleados cobran entre 100 y 300 y cuantos cobran mas de 300.
// Ademas el programa debera informar el importe que gasta la empresa
// en sueldos al personal
Algoritmo Ejercicio34
	// Cuenta cuantos empleados cobran entre cien y trescientos
	CCentreCienTrescientos <- 0
	// Cuenta cuantos empleados cobran mas de trescientos
	CCmasdeTrescientos <- 0
	// Acumulo el sueldo de los que cobran entre cien y trescientos
	AcumuladorSueldoCienTrescientos <- 0
	// Acumulo el sueldo de los que cobran mas de trescientos
	AcumuladorSueldoMasTrescientos <- 0
	// Auxiliar para el while
	aux <- 1
	Escribir 'Cuantos sueldos va a cargar?'
	// Cuantos sueldos voy a cargar
	Leer CSueldosCargar
	Mientras aux<=CSueldosCargar Hacer
		Escribir 'Ingrese el sueldo '
		Leer sueldo
		Si sueldo>=100 Y sueldo<=300 Entonces
			// esto es lo que cobran entre 100 y 300(cantidad de empleados)
			CCentreCienTrescientos <- CCentreCienTrescientos+1
			// ahora acumularia la cantidad de sueldos que cobran estos empleados
			AcumuladorSueldoCienTrescientos <- AcumuladorSueldoCienTrescientos+sueldo
		SiNo
			Si sueldo>300 Entonces
				// esto es lo que cobran mas de 300(cantidad de empleados)
				CCmasdeTrescientos <- CCmasdeTrescientos+1
				// ahora acumularia la cantidad de sueldos que cobran estos empleados
				AcumuladorSueldoMasTrescientos <- AcumuladorSueldoMasTrescientos+sueldo
			FinSi
		FinSi
		// Aumento el contador para evitar que sea infinito el bucle
		aux <- aux+1
	FinMientras
	// Esto es el gasto total en sueldos
	TotalpagoSueldo <- AcumuladorSueldoCienTrescientos+AcumuladorSueldoMasTrescientos
	Escribir 'Cantidad de empleados que cobran entre 100 y 300'
	// mostramos la cantidad de empleados que cobran entre 100 y 300
	Escribir CCentreCienTrescientos
	Escribir 'Cantidad de empleados que cobran mas de 300'
	// mostramos la cantidad de empleados que cobran mas de 300
	Escribir CCmasdeTrescientos
	// mostramos el gasto total en sueldos
	Escribir TotalpagoSueldo
FinAlgoritmo
