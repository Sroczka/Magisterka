# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:31:57 2019

@author: Marta
"""
import numpy as np
import matplotlib.pyplot as plt

from gorny_funkcja_omega3d import *
from dolny_funkcja_omega3d import *

b = 25
n = 3
K = 195
S0 = 190.15
r = 0.0225
sigma = 0.155

prog_zmiany = np.linspace(130,250,121)

N = 100

r1 = 0.015
r2 = 0.03

ceny = np.zeros(np.shape(prog_zmiany)[0])

for i in range(np.shape(prog_zmiany)[0]):
    theta = 0
    phi = 0
    for j in range(N):
        phi += Phi_omega3d(b,n,S0,K,r,sigma,r1,r2,prog_zmiany[i],j*2+10)
        theta += Theta_omega3d(b,n,S0,K,r,sigma,r1,r2,prog_zmiany[i],j*2+10)
    ceny[i] = (theta+phi)/(2*N)
    
plt.plot(prog_zmiany,ceny, color = 'darkmagenta')
plt.ylabel('premia opcji')
plt.xlabel('prog zmiany oprocentowania')
plt.savefig("apple_zmienny_prog.jpg")

#plt.suptitle('Zależnosc premi opcji typu omega clock od progu zmiany oprocentowania')
plt.show()
