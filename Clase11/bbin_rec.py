#%%
def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio]>e:
            res = bbinaria_rec(lista[0:medio],e)
        elif lista[medio]<e:
            res = bbinaria_rec(lista[medio+1:],e)
        else:
            res = True
    return res
