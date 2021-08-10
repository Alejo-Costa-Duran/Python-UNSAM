#solucion_de_errores.py
#Ejercicios de errores en el codigo
#%%
#Ejercicio 3.1: Semántica
#Comentario:Había dos errores y de tipo semántico ubicados en el bucle while. En primer lugar, el codigo solo detecta a minúscula sin tildes. Para arreglar eso modifiqué el if expresion[i] == 'a' por un
# expresión[i] in letra_a donde letra_a es el string letra_a = 'aAÁá', así la función detecta si la expresión tiene la letra a, ya sea minúscula o mayúscula y con tilde os in tilde. Otro error es que la
#devuelve "False" ante la primer letra distinta de "a" que encuentre. Para solucionar eso agregué la variable de tipo bool que llamé "tiene" que inicia siendo falsa y se cambia a verdadera si encuentra 
#una A, la función devuelve esta variable.
#Acá va el código corregido y evaluado en las tres expresiones
def tiene_a(expresion):
	tiene = False
	i=0
	n = len(expresion)
	letra_a = 'aAÁá'
	while i<n and not tiene:
		if expresion[i] in letra_a:
			tiene = True
		i+=1
	return tiene
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: hay dos errores de sintáxis y uno de semántica. Los de sintáxis están en el "return Falso", debería decir "return False" y que falta el ":" luego del if, luego del while y luego del nombre 
#de la función. El de semántica es que no toma mayusculas o tildes 
#Acá va el código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    letra_a = 'aAÁá'
    while i<n:
        if expresion[i] in letra_a:
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.3. Función tiene_uno():
#Tiene un error en tiempo de ejecución. Es un error de tipo ya que la función solo toma si la variable tiene el character "1", no va a funcionar con numeros enteros o floats. Para solucionarlo transformo
#la variable expresion a un string
#Acá va el codigo corregido:

def tiene_uno(expresion):
    expresion_string = str(expresion)
    n = len(expresion_string)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion_string[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%%
#Ejercicio 3.4: Alcances
#Hay un error de sintáxis, la variable "c" solo está definida dentro de la función pero nunca lo tomamos como output de la misma. Lo solucioné agregando "return c" a la función.
#Acá va el código corregido
def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5: Pisando memoria
#Es un error de semántica. Estoy agregando a la lista camion el diccionario registro, pero los valores de registro se van actualizando, así que siempre voy a tener los últimos valores de registro que se tienen
#Lo solucioné definiendo registro dentro del loop foor. Así para cada fila se define un nuevo diccionario registro quien se agregará a la lista
#Acá va el código corregido.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion
camion = leer_camion('../Data/camion.csv')
pprint(camion)