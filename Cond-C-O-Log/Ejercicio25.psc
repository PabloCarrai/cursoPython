// Escribir un programa que pida ingresar la coordenada de un
// punto en el plano, es decir dos valores enteros
// x e y(distinto a cero).Posteriormente imprimir en pantalla
// en que cuadrante se ubica dicho punto
// y>0 x>0 1 cuadrante
// y>0 x<0 2 cuadrante
// y<0 x<0 3 cuadrante
// y<0 x>0 4 cuadrante
Algoritmo Ejercicio25
	Escribir 'Ingrese x'
	Leer cx
	Escribir 'Ingrese y'
	Leer cy
	Si ((cy>0) Y (cx>0)) Entonces
		Escribir 'Primer Cuadrante'
	SiNo
		Si ((cy<0) Y (cx<0)) Entonces
			Escribir 'Segundo Cuadrante'
		SiNo
			Si ((cy<0) Y (cx<0)) Entonces
				Escribir 'Tercer Cuadrante'
			SiNo
				Si ((cy<0) Y (cx>0)) Entonces
					Escribir 'Cuarto Cuadrante'
				SiNo
					Escribir 'Se encuentra sobre un eje'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
