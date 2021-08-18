def buscar_precio(fruta):
	venden_fruta = False #Falso si no venden la fruta/verdura, verdadero si la venden
	with open('../Data/precios.csv','rt') as archivo:
		for fila in archivo:
			datos = fila.split(',')
			if datos[0]==fruta:
				print("El precio de un cajón de "+fruta+" es:",datos[1])
				venden_fruta = True
	if not venden_fruta: #Solo va a entrar al if cuando no se modifique la variable venden_fruta, cuando no la vendan
		print(fruta + ' no figura en el listado de precios')

buscar_precio('Maracuyá')
buscar_precio('Naranja')