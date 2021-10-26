#%% Ejercicio 11.2 Numeros triangulares

def triangular(n):
    '''
    Pre: n debe ser un entero positivo
    Pos: Devuelve la suma de los primeros n
    enteros positivos
    '''
    if n==1:
        res = 1
    else:
        res = n+triangular(n-1)
    return res

print(8//10)

#%% Ejercicio 11.3

def cant_digitos(n):
    '''
    Pre: n entero positivo
    Pos: Devuelve la cantidad de digitos de n
    '''
    if n//10 == 0:
        cant_dig = 1
    else:
        cant_dig = 1 + cant_digitos(n//10)
    return cant_dig

#%% Ejercicio 11.4
def es_potencia(n,b):
    '''
    Pre: n y b enteros positivos
    Pos: Devuelve True si n es potencia de b, False sino
    '''
    a = n/b
    if a==1:
        return True
    elif int(a)!=a:
        return False
    else:
        return es_potencia(a,b)

#%% Ejercicio 11.5
def posiciones_de(a,b):
    def _pos(a,b):
        list_pos = []
        if b not in a:
            return list_pos
        else:
            list_pos = [a.index(b)]+_pos(a[a.index(b)+1:],b)
        return list_pos 
    list_pos = _pos(a,b)
    for i,el in enumerate(list_pos[1:],start=1):
        list_pos[i] += list_pos[i-1]+1
    return list_pos
#%% Ejercicio 11.6
def par(n):
    if n==1:
        return False
    return impar(n-1)
def impar(n):
    if n==1:
        return True
    else:
        return par(n-1)

#%% Ejercicio 11.7

def maximo(lista):
    maxim_ = lista[0]
    if len(lista)==1:
        return lista[0]
    if maxim_>maximo(lista[1:]):
        return maxim_
    else:
        return maximo(lista[1:])

#%% Ejercicio 11.8

def replicar(lista,n):
    list_temp = []
    if len(lista)==1:
        list_temp += [lista[0]]*n
        return list_temp
    else:
        list_temp += [lista[0]]*n+_rep(lista[1:],n)
        return list_temp 

#%% Ejercicio 11.10

def combinaciones(lista,k):
    if len(lista==k):
        
            