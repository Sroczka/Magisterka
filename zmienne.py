# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:15:36 2019

@author: Marta
"""
import numpy as np

b = 10
n = 3
K = 195
S0 = 190.15
r = 0.0225
sigma = 0.155

prog_zmiany = 180

N = 100

r1 = np.linspace(0,0.0225, 100)#arange(0, 0.025, 0.001)
r2 = np.linspace(0.0225, 0.045, 100)#arange(0.025, 0.045, 0.001)
X = np.copy(r1)
Y = np.copy(r2)
X, Y = np.meshgrid(X, Y)

Z = np.zeros([np.shape(r1)[0],np.shape(r2)[0]])
kolumny = list()
for i in range(np.shape(r2)[0]):
        kolumny.append(r2[i])