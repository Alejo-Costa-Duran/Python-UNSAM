def traductor_geringoso(palabra):
	'Traduce el input al geringoso'
	palabra_geringoso = ''
	vocales = 'aeiouu'
	vocales_tildes = 'áéíóúü'
	Umuda = 'QqGg'
	posicion = 0
	for i,letra in enumerate(palabra):
		if letra.lower() in vocales:
			print(palabra[i-1] in Umuda,i-1)
			if letra=='u' and (palabra[i-1] in Umuda) and (i-1)>-1:
				palabra_geringoso += letra
			else:
				palabra_geringoso += letra+'p'+letra.lower()
		elif (letra.lower() in vocales_tildes):
			palabra_geringoso +=letra+'p'+vocales[vocales_tildes.find(letra.lower())]
		else:
			palabra_geringoso += letra
		posicion +=1
		print(palabra_geringoso)
	return palabra_geringoso

def diccionario_geringoso(lista_palabras):
	'Devuelve un diccionario geringoso a partir de una lista de palabras'
	diccionario_geringoso = {}
	for palabras in lista_palabras:
		diccionario_geringoso[palabras] = traductor_geringoso(palabras)
	return diccionario_geringoso

palabras_a_traducir = ['pingüino', 'canción','Alargue']
diccionario = diccionario_geringoso(palabras_a_traducir)
print(diccionario)
