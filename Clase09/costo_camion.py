import informe_final
import sys

def costo_camion(nombre_archivo):
    lista_camion = informe_final.leer_camion(nombre_archivo)
    precio_total_pagado = 0
    for verduras in lista_camion:
        precio_total_pagado += verduras.costo()
    return precio_total_pagado

def f_principal(argumentos):
    print(f'Costo total pagado: {costo_camion(argumentos[1]):.2f}')
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    f_principal(sys.argv)

