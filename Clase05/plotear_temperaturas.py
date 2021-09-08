#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 00:30:48 2021

@author: alejinn
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas  = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=20)
    plt.show()