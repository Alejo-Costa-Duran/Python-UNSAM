#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:19:24 2021

@author: alejinn
"""

import csv

def parse_csv(nombre_archivo,select =None, types= None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        registros = []
        # Lee los encabezados
        if has_headers:
            headers = next(rows)
            if select: 
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                if select:
                    row = [row[indice] for indice in indices]
                if types:
                    row = [func(valor) for func,valor in zip(types,row)]
                registro = dict(zip(headers, row))
                registros.append(registro)
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
