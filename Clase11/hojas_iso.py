#%%
def medidas_hoja_A(N):
    if N==0:
        return (841,1189)
    else:
        ancho_ant,largo_ant = medidas_hoja_A(N-1)
        return (largo_ant//2,ancho_ant)
