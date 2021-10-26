#%%
def pascal(n,k):
    '''
    Pre: n y k enteros mayores a 0 con k menor igual que n
    Pos: Devuelve el numero en la posicion n,k en el triángulo de Pascal
    '''
    if n==k or k==0:
        return 1
    else:
        return pascal(n-1,k-1)+pascal(n-1,k)
