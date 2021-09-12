altura_inicial = 100.0 #Altura inicial medida en metros
altura_rebote_n = altura_inicial #Representa la altura luego del rebote número n
rebote_n=0

while rebote_n<10:
    rebote_n +=1
    altura_rebote_n = 0.6*altura_rebote_n
    print(rebote_n,round(altura_rebote_n,4))
