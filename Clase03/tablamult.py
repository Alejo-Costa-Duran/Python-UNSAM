#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:36:23 2021

@author: alejinn
"""
#%%
header = f'{"":>4s}'
separador = f'{"":->5}'
for i in range(10):
    header += f'{i:>4d}'
    separador += f'{"":->4}'

def multiplos_n(n):
    s=0
    nformat = f'{n:d}:'
    multiplos = f'{nformat:<4s}'
    for i in range(10):
        multiplos += f'{s:>4d}'
        s+=n
    return multiplos

print(header)
print(separador)
for n in range(10):
    print(multiplos_n(n))


