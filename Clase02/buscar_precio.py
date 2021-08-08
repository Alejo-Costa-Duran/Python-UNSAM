def buscar_precio(fruta):
	venden_fruta = False
	with open('../Data/precios.csv','rt') as archivo:
		encabezados = next(archivo)
		for fila in archivo:
			datos = fila.split(',')
			if datos[0]==fruta:
				print("El precio de un cajón de "+fruta+" es:",datos[1])
				venden_fruta = True
				break
	if not venden_fruta:
		print(fruta + ' no figura en el listado de precios')

buscar_precio('Maracuyá')
buscar_precio('Naranja')