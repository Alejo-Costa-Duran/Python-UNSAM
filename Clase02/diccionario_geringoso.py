def traductor_geringoso(palabra):
	'Traduce el input al geringoso'
	palabra_geringoso = ''
	vocales = 'aeiou'
	for letra in palabra:
		palabra_geringoso += letra
		if letra in vocales:
			palabra_geringoso +='p'+letra
	return palabra_geringoso #No funciona bien con palabras con varias vocales juntas

def diccionario_geringoso(lista_palabras):
	'Devuelve un diccionario geringoso a partir de una lista de palabras'
	diccionario_geringoso = {}
	for palabras in lista_palabras:
		diccionario_geringoso[palabras] = traductor_geringoso(palabras)
	return diccionario_geringoso

palabras_a_traducir = ['banana', 'manzana','mandarina']
diccionario = diccionario_geringoso(palabras_a_traducir)
print(diccionario)
