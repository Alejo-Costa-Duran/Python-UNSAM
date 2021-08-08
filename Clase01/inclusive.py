frase = '¿Cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    if len(palabra)>1:
        if palabra[-1]=='o':
            frase_t = frase_t+' '+palabra[:-1]+'e'
        elif palabra[-2]=='o':
            frase_t = frase_t+' '+palabra[:-2]+'e'+palabra[-1]
        else:
            frase_t = frase_t + ' ' + palabra
    else:
        frase_t = frase_t+' '+palabra
frase_t = frase_t.strip()
print(frase_t)
