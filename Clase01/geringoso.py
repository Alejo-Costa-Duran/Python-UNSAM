cadena = 'Boligoma' #Palabra a traducir
vocales = 'aeiou' #Para comprobar si la letra que estoy mirando es una vocal
cadena_traducida = '' #Cadena donde guardo la palabra traducida al geringoso

for letra in cadena:
	if letra in vocales:
		cadena_traducida = cadena_traducida+letra+'p'+letra
	else:
		cadena_traducida = cadena_traducida+letra
print(cadena_traducida)
