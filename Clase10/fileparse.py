#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:19:24 2021

@author: alejinn
"""

import csv

def parse_csv(lines,select =None, types= None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    rows = csv.reader(lines)
    registros = []
    # Lee los encabezados
    if has_headers:
        headers = next(rows)
        if select: 
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        for idx,row in enumerate(rows,start=1):
            if not row:    # Saltea filas sin datos
                continue
            if select:
                row = [row[indice] for indice in indices]
            if types:
                try:
                    row = [func(valor) for func,valor in zip(types,row)]
                    registro = dict(zip(headers, row))
                    registros.append(registro)
                except ValueError as error:
                    if not silence_errors:
                        msg1 = f'Fila {idx:>d}: No pude convertir {row}'
                        msg2 = f'Fila {idx:>d}: Motivo: {error}'
                        print(msg1+'\n'+msg2)
    else:
        if types:
            for row in rows:
                if not row:
                    continue
                registro = tuple([func(cols) for func,cols in zip(types,row)])
                registros.append(registro)
        else:
            for row in rows:
                if not row:
                    continue
                registro = tuple([cols for cols in row])
                registros.append(registro)
    return registros